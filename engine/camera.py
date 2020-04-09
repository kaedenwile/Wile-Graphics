import numpy as np
from copy import deepcopy

from .node import Node
from .mesh import Mesh
from .transform import Transform


class Camera(Node):

    def __init__(self, focal_length, width, height, near_depth, far_depth, transform=Transform.none):
        super(Camera, self).__init__(
            mesh=Mesh(vertices=np.asarray([  # looking down z-axis
                [0, 0, 0],  # center
                [0, 0, focal_length],  # focus
                [width / 2.0, 0, focal_length],  # right
                [0, height / 2.0, focal_length],  # top
            ])), transform=transform)

        self.focal_length = focal_length
        self.width = width
        self.height = height

        self.near_depth = near_depth
        self.far_depth = far_depth

        self.camera_object = None  # the most recent camera object produced by make

    def make(self):
        """
        Returns a Vec3 -- the focal point of the camera,
        followed by an array of the four corners of the screen
        in counterclockwise order starting in the upper right,
        all with the transform applied. The fifth is the center.
        A reference to self is also attached.
        """
        m = deepcopy(self.mesh)
        focus = m.pointer_to(0)
        center = m.pointer_to(1)
        right = m.pointer_to(2)
        top = m.pointer_to(3)

        # def camera_space_transform(mesh):
        #     """Takes the scene mesh and returns a transform that takes
        #     any scene coordinate to a camera coordinate."""
        #     return Transform(np.linalg.solve(
        #         np.stack([
        #             mesh[center] - mesh[focus],
        #             mesh[right] - mesh[focus],
        #             mesh[top] - mesh[focus]
        #         ]),
        #         np.stack([
        #             self.mesh[1],
        #             self.mesh[2],
        #             self.mesh[3]
        #         ])
        #     ), mesh[focus])

        def convert_to_camera(mesh):
            """
            Returns a mesh where each vertex has been flattened
            to an x, y coordinate in the camera plane
            and a distance w from the focus.
            """
            vertices = mesh.vertices

            focus_to_center = mesh[center] - mesh[focus]
            focus_to_vectors = vertices - mesh[focus]

            distances = np.inner(focus_to_center, focus_to_center) / np.dot(focus_to_vectors, focus_to_center)
            in_plane = mesh[focus] + focus_to_vectors * distances[:, None]

            offsets = in_plane - mesh[center]
            x, y = mesh[right] - mesh[center], mesh[top] - mesh[center]
            # x, y = x / np.linalg.norm(x), y / np.linalg.norm(y)  # normalize x and y
            x, y = x / np.inner(x, x), y / np.inner(y, y)  # normalize x and y

            print(offsets.shape, np.asarray([x, y]).T.shape)

            new_vertices = np.concatenate([np.dot(offsets, np.asarray([x, y]).T), distances[:, None]], axis=1)
            return Mesh(new_vertices, mesh.faces, mesh.pointers)

        self.camera_object = {
            "convert_to_camera": convert_to_camera
        }

        return m.join(*(child.make() for child in self.children)).transformed_by(self.transform)
