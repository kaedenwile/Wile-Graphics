import display
from engine import *
from math import pi

import numpy as np

size = width, height = (1280 // 2, 960 // 2)

scene = Scene()

# mesh = Mesh([
#     Vec3(-10, 0, 0),
#     Vec3(0, 0, -5),
#     Vec3(3, 0, 7),
#     Vec3(4, 0, 1),
# ], [(0, 1, 2)])

# mesh = Mesh([
#     Vec3(1, 0, 1),  # TOP RIGHT
#     Vec3(-1, 0, 1),  # TOP LEFT
#     Vec3(-1, 0, -1),  # BOTTOM LEFT
#     Vec3(1, 0, -1),  # BOTTOM RIGHT
# ], [(0, 1, 2), (2, 3, 0)])

mesh = Mesh(np.asarray([
    (1, 1, 1),
    (-1, 1, 1),
    (1, 1, -1),
    (-1, 1, -1),
    (1, -1, 1),
    (-1, -1, 1),
    (1, -1, -1),
    (-1, -1, -1),
]), np.asarray([
    (0, 2, 3), (0, 3, 1),
    (1, 3, 5), (3, 7, 5),
    (2, 7, 3), (2, 6, 7),
    (4, 7, 6), (4, 5, 7),
    (0, 4, 2), (2, 4, 6),
    (0, 5, 1), (0, 4, 5)
]))

# mesh = Mesh(np.asarray([
#     (0, 1, 0),
#     (-1, -1, 0),
#     (1, -1, 0)
# ]), np.asarray([
#     (0, 1, 2)
# ]))

# node = Node(mesh, Transform.of(translation=np.asarray([0, 0, -10]), scaling=np.asarray([50, 50, 50])))
node_rotation = np.asarray([0, 0, pi / 4])
node_scale = np.asarray([1, 1, 1]) * 2
node = Node(mesh, Transform.of(np.asarray([-1, -4, 57]), node_rotation, node_scale))

scene.root.add_child(node)

camera = Camera(4, 4, 3, 1, 100)
scene.root.add_child(camera)
scene.active_camera = camera

should_draw = True


def main_loop(screen):
    global should_draw

    if should_draw:
        screen.draw(scene.render(screen))
        should_draw = False


def key_handler(key):
    global should_draw

    # print("KEY: "+key)

    if key == 'a':
        node.transform.translation[0] -= 1
    elif key == 'd':
        node.transform.translation[0] += 1
    elif key == 'w':
        node.transform.translation[1] += 1
    elif key == 's':
        node.transform.translation[1] -= 1
    elif key == 'q':
        node.transform.translation[2] -= 1
    elif key == 'e':
        node.transform.translation[2] += 1

    if key == 'f':
        node_rotation[2] -= pi / 16
        node.transform = Transform.of(node.transform.translation, node_rotation, node_scale)
    elif key == 'h':
        node_rotation[2] += pi / 16
        node.transform = Transform.of(node.transform.translation, node_rotation, node_scale)
    elif key == 't':
        node_rotation[0] -= pi / 16
        node.transform = Transform.of(node.transform.translation, node_rotation, node_scale)
    elif key == 'g':
        node_rotation[0] += pi / 16
        node.transform = Transform.of(node.transform.translation, node_rotation, node_scale)
    elif key == 'r':
        node_rotation[1] -= pi / 16
        node.transform = Transform.of(node.transform.translation, node_rotation, node_scale)
    elif key == 'y':
        node_rotation[1] += pi / 16
        node.transform = Transform.of(node.transform.translation, node_rotation, node_scale)

    if key == 'u':
        node_scale[0] += 0.25
        node.transform = Transform.of(node.transform.translation, node_rotation, node_scale)
    elif key == 'j':
        node_scale[0] -= 0.25
        node.transform = Transform.of(node.transform.translation, node_rotation, node_scale)
    elif key == 'i':
        node_scale[1] += 0.25
        node.transform = Transform.of(node.transform.translation, node_rotation, node_scale)
    elif key == 'k':
        node_scale[1] -= 0.25
        node.transform = Transform.of(node.transform.translation, node_rotation, node_scale)
    elif key == 'o':
        node_scale[2] += 0.25
        node.transform = Transform.of(node.transform.translation, node_rotation, node_scale)
    elif key == 'l':
        node_scale[2] -= 0.25
        node.transform = Transform.of(node.transform.translation, node_rotation, node_scale)

    elif key == 'z':
        camera.focal_length *= 0.5
        # print(camera.focal_length)
    elif key == 'x':
        camera.focal_length *= 2
        # print(camera.focal_length)

    should_draw = True
    # screen.draw(scene.render(screen))
    # print(node.transform)


display.Screen(*size, title="UW Graphics", frame_rate=60, update=main_loop, callback=key_handler)

# while True:
#     time.sleep(0.5)
#     print("PING")