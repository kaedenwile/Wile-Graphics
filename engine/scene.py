from engine import Transform, Camera
from engine.node import Node


class Scene:

    def __init__(self):
        self.root = Node()

        self.primary_camera = None

    def render(self):
        vertices, edges, faces, cameras = self.make()

        camera = None
        for cam in cameras:
            if cam[2] is self.primary_camera:
                camera = cam
                break


        world_faces = self.w_index(camera, vertices, edges, *self.camera_culling(camera, vertices, edges, faces))

        ## DRAW

    def make(self):
        # apply transformations and children to build a
        # giant list of vertices, edges, and faces

        def make_recursive(node, transform, offsets):
            vertices = []
            edges = []
            faces = []
            cameras = []

            trans = transform.combine(node.transform)

            for vertex in node.mesh.vertices:
                vertices.append(trans.apply(vertex))

            for edge in node.mesh.edges:
                edges.append((edge[0] + offsets[0], edge[1] + offsets[0]))

            for face in node.mesh.faces:
                faces.append((face[0] + offsets[1], face[1] + offsets[1], face[2] + offsets[1]))

            for child in node.children:
                if type(child) is Camera:
                    cameras.append((child.make(trans)))
                else:
                    data = make_recursive(child, trans, (offsets[0] + len(vertices), offsets[1] + len(edges)))
                    vertices += data[0]
                    edges += data[1]
                    faces += data[2]

            return vertices, edges, faces, cameras

        return make_recursive(self.root, Transform.none(), (0, 0))

    @staticmethod
    def camera_culling(camera, vertices, edges, faces):
        camera_2d = camera["2d"]
        camera_width = camera["camera"].width / 2
        camera_height = camera["camera"].height / 2
        focal_point = camera["focal_point"]
        screen_center = camera["center"]

        calc_t = lambda v: (screen_center.x - focal_point.x) / (v.x - focal_point.x)
        calc_intersect = lambda t, v: focal_point + t * (v - focal_point)

        legal_vertices = []
        for vertex in vertices:
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
    def w_index(camera, vertices, edges, faces):
        focus = camera["focal_point"]
        camera_near_sqd = pow(camera["camera"].near_depth, 2)
        camera_far_sqd = pow(camera["camera"].far_depth, 2)

        w_faces = []
        for face in faces:
            verts = []

            for edge in face:
                for vertex in edges[edge]:
                    if vertex not in verts:
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


