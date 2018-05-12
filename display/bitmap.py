import random as rand
import Tkinter as tk


class Bitmap(object):

    def __init__(self, width, height, bits=list()):
        self.width = width
        self.height = height

        if len(bits) == self.width * self.height:
            self.bits = bits
        else:
            self.bits = [(0, 0, 0) for _ in xrange(0, self.width * self.height)]

    def __setitem__(self, key, value):
        index = key[0] + self.width * key[1] + self.height*self.width/2 + self.width/2
        if 0 <= index < len(self.bits):
            self.bits[index] = value

    # def __getitem__(self, key):
    #     return self.bits[key[0] + self.width * key[1]]

    def draw_triangle(self, points, color=None):
        for p in points:
            print(p)

        if not color:
            color = [rand.randint(0, 255) for _ in range(3)]

        # find middle point by x-index
        points.sort(key=lambda p: p.x)

        line1 = lambda x: (points[0].y - points[1].y) / (points[0].x - points[1].x) * (x - points[0].x) + points[0].y if (points[0].x - points[1].x) != 0 else 0
        line2 = lambda x: (points[1].y - points[2].y) / (points[1].x - points[2].x) * (x - points[1].x) + points[1].y if (points[1].x - points[2].x) != 0 else 0
        line3 = lambda x: (points[2].y - points[0].y) / (points[2].x - points[0].x) * (x - points[2].x) + points[2].y if (points[2].x - points[0].x) != 0 else 0

        x_vals = map(lambda p: p.x, points)
        min_x = min(x_vals)
        max_x = max(x_vals)

        for x in xrange(int(min_x), int(max_x)):
            if x < points[1].x:
                y_0 = int(line1(x))
            else:
                y_0 = int(line2(x))
            y_1 = int(line3(x))

            for y in xrange(min(y_0, y_1), max(y_0, y_1)):
                self[(x, y)] = color

    def image(self):
        img = tk.PhotoImage(width=self.width, height=self.height)

        row = 0
        col = 0
        for color in self.bits:
            img.put('#%02x%02x%02x' % tuple(color), (row, self.width - col))

            col += 1
            if col == self.height:
                row += 1
                col = 0

        return img

    @staticmethod
    def random(screen):
        return Bitmap(screen.width, screen.height, [[rand.randint(0, 255) for _ in xrange(0, 3)] for _ in xrange(0, screen.width * screen.height)])

    @staticmethod
    def fill(screen, color):
        return Bitmap(screen.width, screen.height, [color for _ in xrange(0, screen.width * screen.height)])