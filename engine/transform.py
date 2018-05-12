from algebra import Vec3, Mat3
import math


# TRANSFORMATIONS happen in this order:
#
#   scaling
#   rotation // in radians
#   translation
#
class Transform:

    def __init__(self, translation, rotation, scaling):
        scale = Mat3([
            scaling[0], 0, 0,
            0, scaling[1], 0,
            0, 0, scaling[2]])

        sin = list(map(lambda theta: math.sin(theta), rotation))
        cos = list(map(lambda theta: math.cos(theta), rotation))
        x_rot = Mat3([
            1, 0, 0,
            0, cos[0], -sin[0],
            0, sin[0], cos[0]])
        y_rot = Mat3([
            cos[1], 0, sin[1],
            0, 1, 0,
            -sin[1], 0, cos[1]])
        z_rot = Mat3([
            cos[2], -sin[2], 0,
            sin[2], cos[2], 0,
            0, 0, 1
        ])

        self.matrix = scale * x_rot * y_rot * z_rot
        self.translation = translation


    def apply(self, vertex):
        return self.matrix * vertex + translation


    @staticmethod
    def none():
        return Transform(Vec3.zero(), Vec3.zero(), Vec3.zero())
