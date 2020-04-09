from PIL import Image, ImageTk
import numpy as np


class Bitmap:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.bits = np.zeros((self.height, self.width, 4), np.uint8)

        self.ys = np.repeat(np.arange(self.height)[:, None], self.width, axis=1)
        self.scale = np.array([self.width / 2.0, self.height / 2.0, 1])
        self.offset = np.array([1, 1, 0])

    def draw_triangle(self, points, color):
        """
        points -- np.array with shape (3, 3). point[0, :] = x, y, w
        """
        if np.any(np.isnan(points)):
            return

        color = np.random.random(3) * 255
        # points = (points + self.offset) * self.scale
        points = (points + self.offset) * self.scale

        l, m, r = np.argsort(points[:, 0])
        left, mid, right = points[l], points[m], points[r]

        left_x = clamp(0, int(left[0]), self.width)
        mid_x = clamp(0, int(mid[0]), self.width)
        right_x = clamp(0, int(right[0]), self.width)

        in_triangle = np.zeros((self.height, self.width), np.bool)

        left_to_right = self._line_between(left, right)
        if left_to_right is None:
            return  # not a triangle, just a line

        if (left_to_mid := self._line_between(left, mid)) is not None:
            in_triangle[:, left_x:mid_x] = np.logical_xor(self.ys < left_to_mid, self.ys < left_to_right)[:,
                                           left_x:mid_x]

        if (mid_to_right := self._line_between(mid, right)) is not None:
            in_triangle[:, mid_x:right_x] = np.logical_xor(self.ys < mid_to_right, self.ys < left_to_right)[:,
                                            mid_x:right_x]

        self.bits[in_triangle, :3] = color

    def _line_between(self, p1, p2):
        x1, y1 = p1[:2]
        x2, y2 = p2[:2]

        if np.isclose(x1, x2):
            return None
        elif np.isclose(y1, y2):
            return np.full(self.width, y1)
        else:
            m = (y1 - y2) / (x1 - x2)
            b = y1 - m * x1
            return m * np.arange(self.width) + b

    def image(self):
        img = Image.fromarray(self.bits[::-1, :, :3])
        return ImageTk.PhotoImage(img)


def clamp(minimum, n, maximum):
    return max(min(n, maximum), minimum)
