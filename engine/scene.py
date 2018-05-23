import math

from algebra import Vec3
from display import Bitmap

from vertex import Vertex

from transform import Transform
from camera import Camera
from node import Node


class Scene(object):

    def __init__(self):
        self.root = Node()

        self.primary_camera = None

    def render(self, screen):
        vertices, faces, cameras = self.apply_transform()

        transformed_camera = None
        for cam in cameras:
            if cam["camera"] is self.primary_camera:
                transformed_camera = cam
                break

        vertices = self.make(transformed_camera, vertices, faces)

        world_faces = self.w_index(transformed_camera, vertices,
                                   self.camera_culling(self.primary_camera, vertices, faces))

        # DRAW
        bitmap = Bitmap(screen.width, screen.height)
        for face in world_faces:
            bitmap.draw_triangle(map(lambda v: vertices[v].screen, face))

        return bitmap

    def apply_transform(self):
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
    def make(camera, vertices, faces):

        find_intersect = camera["intersect"]
        convert_2d = camera["2d"]

        def build_vertex(world):
            intersect, t = find_intersect(world)
            # print(intersect)
            return Vertex(world, convert_2d(intersect), t)

        new_vertices = list(map(build_vertex, vertices))

        # def build_face(face):
        #     pass
        #
        # new_faces = list(map(build_face, faces))

        return new_vertices  #, new_faces

    @staticmethod
    def camera_culling(camera, vertices, faces):
        """
        Does culling based on if vertexes are in the
        \"Pyramid\" of the camera.
        """

        return faces

        # legal_vertices = []
        # for i in range(len(vertices)):
        #     vertex = vertices[i]
        #
        #     if math.isnan(vertex.t) or vertex.t < 0:
        #         print("LESS THAN ONE")
        #         continue
        #
        #     if not (abs(vertex.screen.x) <= 1 and abs(vertex.screen.y) <= 1):
        #         print("OUTSIDE BOUNDS")
        #         continue
        #
        #     legal_vertices.append(i)
        #
        # new_faces = []
        # for face in faces:
        #     if any(v in legal_vertices for v in face):
        #         new_faces.append(face)
        #
        # return new_faces

    @staticmethod
    def w_index(camera_info, vertices, faces):
        """Does culling and sorting based on
        distance from camera.
        """

        focus = camera_info["focus"]
        camera = camera_info["camera"]
        # camera_far_sqd = math.pow(.far_depth, 2)
        # camera_near_sqd = math.pow(camera_info["camera"].near_depth, 2)

        w_faces = []
        for face in faces:
            max_x, min_x = float('-inf'), float('inf')
            max_y, min_y = float('-inf'), float('inf')
            max_z, min_z = float('-inf'), float('inf')

            for vertex in face:
                v = vertices[vertex].world

                if v.x > max_x:
                    max_x = v.x
                if v.x < min_x:
                    min_x = v.x

                if v.y > max_y:
                    max_y = v.y
                if v.y < min_y:
                    min_y = v.y

                if v.z > max_z:
                    max_z = v.z
                if v.z < min_z:
                    min_z = v.z

            center = Vec3((max_x+min_x) / 2, (max_y+min_y) / 2, (max_z+min_z) / 2)

            w_index = (center - focus).length_squared()
            w_faces.append((face, w_index))

        # drop near and far
        # w_faces = filter(lambda w: camera.near_depth < w[1] < camera.far_depth, w_faces)
        w_faces.sort(key=lambda w: w[1], reverse=True)

        return list(map(lambda w: w[0], w_faces))


