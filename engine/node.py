from engine.mesh import Mesh
from engine.shader import Shader
from engine.transform import Transform


class Node:

    def __init__(self, mesh=Mesh.empty(), transform=Transform.none(), shader=Shader("#ffffff")):
        self.children = []

        self.mesh = mesh
        self.transform = transform
        self.shader = shader

    def add_child(self, node):
        self.children.append(node)

