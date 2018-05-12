from engine.node import Node
from engine.transform import Transform
from algebra.vec3 import Vec3


class Camera(Node):

    def __init__(self, focal_length, width, height, near_depth, far_depth, transform=Transform.none()):
        Node.__init__(self, transform=transform)

        self.focal_length = focal_length
        self.width = width
        self.height = height

        self.near_depth = near_depth
        self.far_depth = far_depth
        # self.transform = transform
