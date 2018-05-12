import random as rand
import Tkinter as tk


class Bitmap:

    def __init__(self, screen, bits):
        self.image = tk.PhotoImage(width=screen.width, height=screen.height)

        row = 0
        col = 0
        for color in bits:
            # self.image.put('#%02x%02x%02x' % tuple(color), (row, col))
            self.image.put(color, (row, col))
            col += 1
            if col == screen.height:
                row += 1
                col = 0

        print self.image

    @staticmethod
    def random(screen):
        return Bitmap(screen, [[rand.randint(0, 255) for _ in xrange(0, 3)] for _ in xrange(0, screen.width * screen.height)])

    @staticmethod
    def fill(screen, color):
        return Bitmap(screen, [color for _ in xrange(0, screen.width * screen.height)])