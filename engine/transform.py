from dataclasses import dataclass
import numpy as np


# TRANSFORMATIONS happen in this order:
#
#   scaling
#   rotation // in radians
#   translation
#
@dataclass(frozen=True)
class Transform:
    transform: np.array  # 3x3
    translation: np.array  # 1x3

    def apply(self, vertices):
        return vertices @ self.transform + self.translation

    def combine(self, other):
        return Transform(self.transform * other.transform, other.translation + self.translation)

    @staticmethod
    def of(translation=np.zeros(3), rotation=np.zeros(3), scaling=np.ones(3)):
        scale = np.diag(scaling)
        # [[scaling[0], 0, 0],
        #  [0, scaling[1], 0],
        #  [0, 0, scaling[2]]]

        sin = np.sin(rotation)
        cos = np.cos(rotation)
        x_rot = np.asarray([
            [1, 0, 0],
            [0, cos[0], -sin[0]],
            [0, sin[0], cos[0]]])
        y_rot = np.asarray([
            [cos[1], 0, sin[1]],
            [0, 1, 0],
            [-sin[1], 0, cos[1]]])
        z_rot = np.asarray([
            [cos[2], -sin[2], 0],
            [sin[2], cos[2], 0],
            [0, 0, 1]])

        return Transform(x_rot @ y_rot @ z_rot @ scale, translation)


Transform.none = Transform.of()
