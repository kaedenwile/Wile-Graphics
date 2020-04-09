from algebra import Vec3
from display import Bitmap

from .shader import Shader
from .transform import Transform
from .camera import Camera
from .node import Node


class Scene:

    def __init__(self):
        self.root = Node()

        self.active_camera = None

    def render(self, screen):
        # Flattens children of root node into a single mesh
        mesh = self.root.make()
        transformed_camera = self.active_camera.camera_object

        camera_mesh = transformed_camera['convert_to_camera'](mesh)

        # DRAW
        bitmap = Bitmap(screen.width, screen.height)
        for p1, p2, p3 in mesh.faces:
            bitmap.draw_triangle(camera_mesh[p1, p2, p3], Shader.white)

        return bitmap

    # @staticmethod
    # def make(camera, vertices):
    #
    #     find_intersect = camera["intersect"]
    #     convert_2d = camera["2d"]
    #
    #     def build_vertex(world):
    #         intersect, t = find_intersect(world)
    #         # print(intersect)
    #         return Vertex(world, convert_2d(intersect), t)
    #
    #     new_vertices = list(map(build_vertex, vertices))

    # def build_face(face):
    #     pass
    #
    # new_faces = list(map(build_face, faces))

    # return new_vertices  #, new_faces

    # TODO skippping this, going to write to conditionally write to bitmap based on w index

    # @staticmethod
    # def camera_culling(camera, vertices, faces):
    #     """
    #     Does culling based on if vertexes are in the
    #     \"Pyramid\" of the camera.
    #     """
    #
    #     return faces

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

    # @staticmethod
    # def w_index(camera_info, vertices, faces):
    #     """Does culling and sorting based on
    #     distance from camera.
    #     """
    #
    #     focus = camera_info["focus"]
    #
    #     camera = camera_info["camera"]
    #     camera_far_sqd = pow(camera.far_depth, 2)
    #     camera_near_sqd = pow(camera.near_depth, 2)
    #
    #     w_faces = []
    #     for face in faces:
    #         max_x, min_x = float('-inf'), float('inf')
    #         max_y, min_y = float('-inf'), float('inf')
    #         max_z, min_z = float('-inf'), float('inf')
    #
    #         for vertex in face.verts:
    #             v = vertices[vertex].world
    #
    #             if v.x > max_x:
    #                 max_x = v.x
    #             if v.x < min_x:
    #                 min_x = v.x
    #
    #             if v.y > max_y:
    #                 max_y = v.y
    #             if v.y < min_y:
    #                 min_y = v.y
    #
    #             if v.z > max_z:
    #                 max_z = v.z
    #             if v.z < min_z:
    #                 min_z = v.z
    #
    #         center = Vec3((max_x+min_x) / 2, (max_y+min_y) / 2, (max_z+min_z) / 2)
    #
    #         w_index = (center - focus).length_squared()
    #         w_faces.append((face, w_index))
    #
    #     # drop near and far
    #     w_faces = filter(lambda w: camera_near_sqd < w[1] < camera_far_sqd, w_faces)
    #     w_faces.sort(key=lambda w: w[1], reverse=True)
    #
    #     return list(map(lambda w: w[0], w_faces))
