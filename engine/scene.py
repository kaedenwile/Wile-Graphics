from engine.node import Node


class Scene:

    def __init__(self):
        self.root = Node()

        self.primary_camera = None

    def make(self):


        # apply transformations and children to build a
        # giant list of vertices, edges, and faces
        pass

    def sort_windex(self, camera, dataset):
        vertices = dataset[0]  # each vertex is a Vec3 object
        edges = dataset[1]  # each edge has 2 indices which correspond to vertices
        faces = dataset[2]  # each face has 3 indices, which correspond to edges (ex: [1,2,3])

        # camera.position
        for face in faces:
            verts = []

            for edge in face:
                for vertex in edges[edge]:
                    verts.append(vertices[vertex])

            for vert in verts:



        windex_faces = []  # each windex face has 4 indices, the last of which is the w-index
        ## Make w-indices

        ## sort windex faces by w-index

        return windex_faces



    def filter_vertices(self):
        screen_vec = self.primary_camera.get_screen_vectors()
        vertices = []
        node = self.root



