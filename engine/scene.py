from display import Bitmap
from transform import Transform
from camera import Camera
from node import Node


class Scene(object):

    def __init__(self):
        self.root = Node()

        self.primary_camera = None

    def render(self):
        vertices, faces, cameras = self.make()

        camera = None
        for cam in cameras:
            if cam["camera"] is self.primary_camera:
                camera = cam
                break

        world_faces = self.w_index(camera, vertices, self.camera_culling(camera, vertices, faces))

        ## DRAW
        bitmap = Bitmap(camera["camera"].width, camera["camera"].height)
        # for face in world_faces:
        for face in faces:
            bitmap.draw_triangle(map(lambda v: camera["2d"](vertices[v]), face), (255, 0, 0))

        return bitmap

    def make(self):
        # apply transformations and children to build a
        # giant list of vertices and faces

        def make_recursive(node, transform, offset):
            vertices = []
            faces = []
            cameras = []

            trans = transform.combine(node.transform)

            for vertex in node.mesh.vertices:
                vertices.append(trans.apply(vertex))

            for face in node.mesh.faces:
                faces.append((face[0] + offset, face[1] + offset, face[2] + offset))

            for child in node.children:
                if type(child) is Camera:
                    cameras.append((child.make(trans)))
                else:
                    data = make_recursive(child, trans, (offset + len(vertices)))
                    vertices += data[0]
                    faces += data[1]

            return vertices, faces, cameras

        return make_recursive(self.root, Transform.none(), 0)

    @staticmethod
    def camera_culling(camera, vertices, faces):
        """Does culling based on if vertexes are in the
        \"Pyramid\" of the camera.
        """
        camera_2d = camera["2d"]
        camera_width = camera["camera"].width / 2
        camera_height = camera["camera"].height / 2
        focal_point = camera["focal_point"]
        screen_center = camera["center"]

        calc_t = lambda v: (screen_center.x - focal_point.x) / (v.x - focal_point.x) if v.x != focal_point.x else \
                    (screen_center.y - focal_point.y) / (v.y - focal_point.y)
        calc_intersect = lambda t, v: focal_point + t * (v - focal_point)

        legal_vertices = []
        for vertex in vertices:
            if vertex == focal_point:
                continue

            t = calc_t(vertex)
            if t < 1:
                continue

            intersect = calc_intersect(t, vertex)
            pos_2d = camera_2d(intersect)
            if not (abs(pos_2d.x) < camera_width and abs(pos_2d.y) < camera_height):
                continue

            legal_vertices.append(vertex)



        return faces

    @staticmethod
    def w_index(camera, vertices, faces):
        """Does culling and sorting based on
        distance from camera.
        """
        focus = camera["focal_point"]
        camera_near_sqd = pow(camera["camera"].near_depth, 2)
        camera_far_sqd = pow(camera["camera"].far_depth, 2)

        w_faces = []
        for face in faces:
            verts = []

            for vertex in face:
                if vertices[vertex] not in verts:
                    verts.append(vertices[vertex])

            x = sum(map(lambda v: v.x, verts)) / len(verts)
            y = sum(map(lambda v: v.y, verts)) / len(verts)
            z = sum(map(lambda v: v.z, verts)) / len(verts)

            # TODO make relative to screen
            w_index = (pow((x - focus.x), 2) +
                       pow((y - focus.y), 2) +
                       pow((z - focus.z), 2))

            w_faces.append((face, w_index))

        # drop near and far
        w_faces = filter(lambda w: camera_near_sqd < w[1] < camera_far_sqd, w_faces)
        w_faces.sort(key=lambda w: w[1], reverse=True)

        return list(map(lambda w: w[1], w_faces))


