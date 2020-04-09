from typing import List
from dataclasses import dataclass, field
from copy import deepcopy

from .mesh import Mesh
from .shader import Shader
from .transform import Transform


@dataclass
class Node:
    mesh: Mesh = Mesh.empty
    transform: Transform = Transform.none
    shader: Shader = Shader.white

    children: List['Node'] = field(default_factory=list, init=False)
    is_object: bool = field(default=False, init=False)

    def add_child(self, node: 'Node'):
        self.children.append(node)

    def make(self):
        """
        Returns a single mesh containing all children meshes in this node's parent's coordinate system.
        """
        return deepcopy(self.mesh).join(*(child.make() for child in self.children)).transformed_by(self.transform)
