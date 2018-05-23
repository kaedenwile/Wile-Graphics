import math
import random as rand
import Tkinter as tk
from PIL import Image, ImageTk
import numpy

from algebra import Vec2


class Bitmap(object):

    def __init__(self, width, height, bits=list()):
        self.width = width
        self.height = height

        if len(bits) == self.width * self.height:
            self.bits = bits
        else:
            # self.bits = [[(0, 0, 0) for _ in xrange(0, self.width)] for _ in xrange(0, self.height)]
            # self.bits = [(0, 0, 0) for _ in xrange(0, self.width * self.height)]
            self.bits = numpy.zeros((self.height, self.width, 3), numpy.uint8)

    def __setitem__(self, key, value):
        row, start_col, end_col = key
        # index = key[0] + self.width * key[1]  # + self.height*self.width/2 # + self.width/2
        #
        # if 0 <= index < len(self.bits):
        #     self.bits[index] = value
        self.bits[self.height - end_col:self.height - start_col, row, :] = value

    def __getitem__(self, key):
        return self.bits[key[0] + self.width * key[1]]

    def draw_triangle(self, points, color=None):
        points = list(map(lambda p: Vec2((p.x + 1) * self.width / 2.0, (p.y + 1) * self.height / 2.0), points))

        if not color:
            color = [rand.randint(0, 255) for _ in range(3)]

        # find middle point by x-index
        points.sort(key=lambda p: p.x)

        line1 = lambda x: (points[0].y - points[1].y) / (points[0].x - points[1].x) * (x - points[0].x) + points[0].y \
            if abs(points[0].x - points[1].x) > 0.00001 else float("nan")
        line2 = lambda x: (points[1].y - points[2].y) / (points[1].x - points[2].x) * (x - points[1].x) + points[1].y \
            if abs(points[1].x - points[2].x) > 0.00001 else float("nan")
        line3 = lambda x: (points[2].y - points[0].y) / (points[2].x - points[0].x) * (x - points[2].x) + points[2].y \
            if abs(points[2].x - points[0].x) > 0.00001 else float("nan")

        x_vals = map(lambda p: p.x, points)
        min_x = min(x_vals)
        max_x = max(x_vals)

        for x in xrange(int(min_x), int(max_x)):
            if not 0 < x < self.width:
                continue

            if x < points[1].x:
                y_0 = line1(x)
                if math.isnan(y_0):
                    y_0 = line2(x)
            else:
                y_0 = line2(x)
                if math.isnan(y_0):
                    y_0 = line1(x)

            y_1 = line3(x)
            if math.isnan(y_1) or math.isnan(y_0):
                continue

            y_0 = clamp(0, y_0, self.height)
            y_1 = clamp(0, y_1, self.height)

            min_y = int(math.floor(min(y_0, y_1)))
            max_y = int(math.ceil(max(y_0, y_1)))

            self[x, min_y, max_y] = color

    def image(self):
        img = Image.fromarray(self.bits)
        return ImageTk.PhotoImage(img)

    # @staticmethod
    # def random(screen):
    #     return Bitmap(screen.width, screen.height, [[rand.randint(0, 255) for _ in xrange(0, 3)] for _ in xrange(0, screen.width * screen.height)])
    #
    # @staticmethod
    # def fill(screen, color):
    #     return Bitmap(screen.width, screen.height, [color for _ in xrange(0, screen.width * screen.height)])


def clamp(minimum, n, maximum):
    return max(min(n, maximum), minimum)