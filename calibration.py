import display
from display import Bitmap
from engine import *

import numpy as np

size = width, height = (1280 // 2, 960 // 2)


def main_loop(screen):
    bitmap = Bitmap(screen.width, screen.height)

    bitmap.draw_triangle(np.asarray([
        [1 / width, -1 / height, 5],
        [1 / width, 1 / height, 6],
        [-1 / width, 1 / height, 0],
    ]) * 100, Shader.white)

    screen.draw(bitmap)


def abc(key):
    print("KEY PRESSED", key)


display.Screen(*size, title="Calibrate", frame_rate=60, update=main_loop, callback=abc)
