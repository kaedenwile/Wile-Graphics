

class Mesh:

    def __init__(self, vertices, edges, faces):
        self.vertices = vertices  # Vec3
        self.edges = edges  # Vec2 <- indices of vertices
        self.faces = faces  # Vec3 <- indices of edges

    @staticmethod
    def empty():
        return Mesh([], [], [])
