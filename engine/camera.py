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

    def make(self, transform):
        """
        Returns a Vec3 -- the focal point of the camera,
        followed by an array of the four corners of the screen
        in counterclockwise order starting in the upper right,
        all with the transform applied.
        A reference to self is also attached.
        """

        w = self.width / 2
        h = self.height / 2
        f = self.focal_length

        return transform.apply(Vec3.zero()), list(map(transform.apply, [
            Vec3(w, f, h),
            Vec3(-w, f, h),
            Vec3(-w, f, -h),
            Vec3(w, f, -h),
        ])), self
