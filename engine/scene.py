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




