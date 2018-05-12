from engine.node import Node


class Scene:

    def __init__(self):
        self.root = Node()

        self.primary_camera = None

    def make(self):
        # apply transformations and children to build a
        # giant list of vertices, edges, and faces

        vertices = []
        edges = []
        faces = []

        pass

    def _make_recursive(self, node, translation):
        pass

    def sort_windex(self, camera, dataset):
        vertices = dataset[0]  # each vertex is a Vec3 object
        edges = dataset[1]  # each edge has 2 indices which correspond to vertices
        faces = dataset[2]  # each face has 3 indices, which correspond to edges (ex: [1,2,3])

        for face in faces:
            verts = []

            for edge in face:
                for vertex in edges[edge]:
                    if vertex not in verts:
                        verts.append(vertices[vertex])

            x = 0
            y = 0
            z = 0

            for vertex in verts:
                x += vertex[0]
                y += vertex[1]
                z += vertex[0]

            x = x/3
            y = y/3
            z = z/3
            wcoordinate = [x, y, z]
            # camera.position

            wnumber = (Math.pow((wcoordinate[0]-camera.position[0]), 2)
                                + Math.pow((wcoordinate[1]-camera.position[1]), 2) +
                                Math.pow((wcoordinate[2]-camera.position[2]), 2))

        windex_faces = []  # each windex face has 4 indices, the last of which is the w-index
        for vertex in verts:
            windex_faces.append(vertex)

        windex.append(wnumber)


        ## sort windex faces by w-index

        return windex_faces

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





            


