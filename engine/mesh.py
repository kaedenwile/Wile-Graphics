from dataclasses import dataclass, field
from itertools import accumulate, chain
from typing import List, Tuple
import numpy as np


@dataclass()
class Mesh:
    """A Mesh containing vertices, faces, and pointers to vertices."""
    vertices: np.array = field(default_factory=lambda: np.empty((0, 3)))
    faces: np.array = field(default_factory=lambda: np.empty((0, 3), dtype=np.int))
    pointers: List['VertexPointer'] = field(default_factory=list)

    def transformed_by(self, transform):
        return Mesh(transform.apply(self.vertices), self.faces, self.pointers)

    def join(self, *others):
        all_vertices, all_faces, all_pointers = [self.vertices], [self.faces], [self.pointers]

        cum_vertex_counts = accumulate(map(lambda m: m.vertices.shape[0], [self, *others]))
        for mesh, cum_count in zip(others, cum_vertex_counts):  # zipping without self will give desired 1-offset
            all_vertices.append(mesh.vertices)
            all_faces.append(mesh.faces + cum_count)
            all_pointers.append([p.advanced_by(cum_count) for p in mesh.pointers])

        return Mesh(np.concatenate(all_vertices), np.concatenate(all_faces), list(chain.from_iterable(all_pointers)))

    def pointer_to(self, index):
        vp = VertexPointer(index)
        self.pointers.append(vp)
        return vp

    def __getitem__(self, item):
        if type(item) == VertexPointer:
            return self.vertices[item.vertIndex]
        elif type(item) == int or type(item) == np.int64:
            return self.vertices[item]
        elif type(item) == tuple:
            return np.asarray([self[i] for i in item])
        else:
            raise ValueError("Cannot get vertex with index of type " + str(type(item)))


@dataclass()
class VertexPointer:
    """
    A vertex-pointer allows special objects like cameras or lights
    to reference a specific vertex where they're at, while those
    vertices get transformed and flattened into parent meshes.

    WARNING: this is mutable class, so vertex pointers should only
    be created from deep copies of meshes (during make process)
    """
    vertIndex: int

    def advanced_by(self, newIndex):
        self.vertIndex += newIndex
        return self


Mesh.empty = Mesh()
