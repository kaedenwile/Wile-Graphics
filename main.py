import display
from algebra import Vec3, Mat3
from engine import *
import time

# size = width, height = 640, 480
#
# scene = Scene()
#
# camera = Camera(0.1, 640, 480, 1, 100)
# scene.primary_camera = camera
# scene.root.add_child(camera)
#
# mesh = Mesh([
#     Vec3(-1, 1, 0),
#     Vec3(1, 1, 0),
#     Vec3(-1, -1, 0),
# ], [(0, 1), (1, 2), (2, 0)],
#    [(0, 1, 2)])
# node = Node(mesh, Transform(Vec3(0, 0, 5), Vec3.zero(), Vec3.zero()))
# scene.root.add_child(node)
#
# i = 0
# def main_loop(screen):
#     global i
#     # time.sleep(0.05)
#     screen.draw(display.Bitmap.fill(screen, "#000000" if i%2 == 0 else "#FFFFFF"))
#     print("WOOT WOOT")
#     i += 1
#
#
# display.Screen(*size, title="UW Graphics", update=main_loop)

a = Mat3([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(a)
print

b = Mat3([7, 8, 9, 4, 5, 6, 1, 2, 3])
print(b)
print

print (a * b)