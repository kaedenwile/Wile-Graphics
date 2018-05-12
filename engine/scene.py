from engine.node import Node


class Scene:

    def __init__(self):
        self.root = Node()

        self.primary_camera = None

    def make(self):


        # apply transformations and children to build a
        # giant list of vertices, edges, and faces
        pass


    def filter_vertices(self):
        screen_vec = self.primary_camera.get_screen_vectors()
        vertices = []
        node = self.root



