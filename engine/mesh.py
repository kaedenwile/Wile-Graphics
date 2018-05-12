

class Mesh(object):

    def __init__(self, vertices, faces):
        self.vertices = vertices  # Vec3
        self.faces = faces  # Vec3 <- indices of vertices

    @staticmethod
    def empty():
        return Mesh([], [])
