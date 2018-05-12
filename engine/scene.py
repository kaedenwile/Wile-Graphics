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

        return Scene._make_recursive(self.root, Transform.none(), (0, 0))

    @staticmethod
    def _make_recursive(node, transform, offsets):
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
                data = Scene._make_recursive(child, trans, (offsets[0] + len(vertices), offsets[1] + len(edges)))
                vertices += data[0]
                edges += data[1]
                faces += data[2]

        return vertices, edges, faces, cameras

    @staticmethod
    def camera_culling(camera, vertices, edges, faces):
        return faces

    @staticmethod
    def w_index(camera, vertices, edges, faces):
        focus = camera[0]
        camera_near = camera[2].near_depth
        camera_far = camera[2].far_depth

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
        w_faces = filter(lambda w: camera_near < w[1] < camera_far, w_faces)
        w_faces.sort(key=lambda w: w[1], reverse=True)

        return list(map(lambda w: w[1], w_faces))

    def filter_vertices(self, camera_position, screen_points, vertices):
        rel_v = map(lambda x: x - camera_position, screen_points)

        camera_basis_vector = Vec3((rel_v[0].x + rel_v[1].x) / 2, self.primary_camera.focal_length, (rel_v[0].z + rel_v[3].z) / 2)
        plane_constant = camera_basis_vector.dot(rel_v[0])


        def check(vertex):
            dot = camera_basis_vector.dot(vertex)
            sign = dot / abs(dot)
            if sign > 0:
                t = plane_constant / dot
                v = t * vertex # intercept vector
                return v.x < rel_v[0].x and v.x > rel_v[1].x and v.z < rel_v[0].z and v.z > rel_v[3].z
            else:
                return False

        return list(map(lambda x: check(x), vertices))


        # def get_far_vector(v, far_depth):
        #
        # far_depth_vectors = map(lambda x: get_far_vector(x, self.primary_camera.far_depth), relative_vectors)





            


