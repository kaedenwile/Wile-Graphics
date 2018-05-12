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

    def draw_triangle(self, points, color):
        for p in points:
            print(p)
        # do it to it
        pass

    def image(self):
        img = tk.PhotoImage(width=self.width, height=self.height)

        row = 0
        col = 0
        for color in self.bits:
            self.image.put('#%02x%02x%02x' % tuple(color), (row, col))
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