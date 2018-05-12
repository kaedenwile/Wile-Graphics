import display
from algebra import Vec3, Mat3
from engine import *
import time

size = width, height = 640, 480

scene = Scene()

camera = Camera(0.1, 640, 480, 1, 100)
scene.primary_camera = camera
scene.root.add_child(camera)

mesh = Mesh([
    Vec3(-7, 0, 0),
    Vec3(0, 0, -5),
    Vec3(3, 0, 7),
], [(0, 1, 2)])
node = Node(mesh, Transform.make(Vec3(0, 5, 0), Vec3.zero(), Vec3.zero()))
scene.root.add_child(node)

camera = Camera(1, 20, 20, 1, 20)
scene.root.add_child(camera)
scene.primary_camera = camera

# i = 0


def main_loop(screen):
    # global i
    # time.sleep(0.05)
    print("DRAWING")
    screen.draw(scene.render())
    # i += 1


display.Screen(*size, title="UW Graphics", update=main_loop)