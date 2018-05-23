import display
from algebra import Vec3, Mat3
from engine import *
from math import pi

size = width, height = 1280, 960

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

mesh = Mesh([
    Vec3(1, 1, 1),
    Vec3(-1, 1, 1),
    Vec3(1, 1, -1),
    Vec3(-1, 1, -1),
    Vec3(1, -1, 1),
    Vec3(-1, -1, 1),
    Vec3(1, -1, -1),
    Vec3(-1, -1, -1),
], [
    (0, 2, 3), (0, 3, 1),
    (1, 3, 5), (3, 7, 5),
    (2, 7, 3), (2, 6, 7),
    (4, 7, 6), (4, 5, 7),
    (0, 4, 2), (2, 4, 6),
    (0, 5, 1), (0, 4, 5)
])

node_rotation = Vec3(0, 0, pi/4)
node_scale = Vec3(1, 1, 1) * 2

# node = Node(mesh, Transform.make(Vec3(-2, 20, -3), Vec3(0, 0, 0), Vec3(1, 1, 1) ))
node = Node(mesh, Transform.make(Vec3(5, 20, 3), node_rotation, node_scale))
# node3 = Node(mesh, Transform.make(Vec3(2, 10, 0), Vec3(0, 0, 0), Vec3(1, 1, 1) * 2))

# node = Node(mesh, Transform.make(Vec3(0, 5, 0), Vec3(-0.6, 0.8, -0.5), Vec3(9, 1, 9)))

scene.root.add_child(node)
# scene.root.add_child(node2)
# scene.root.add_child(node3)

# camera = Camera(0.05, 0.5, 0.375, 1, 100)
camera = Camera(2, 4, 3, 1, 100)
scene.root.add_child(camera)
scene.primary_camera = camera

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
        node.transform.translation.x -= 1
    elif key == 'd':
        node.transform.translation.x += 1
    elif key == 'w':
        node.transform.translation.z += 1
    elif key == 's':
        node.transform.translation.z -= 1
    elif key == 'q':
        node.transform.translation.y -= 1
    elif key == 'e':
        node.transform.translation.y += 1

    if key == 'f':
        node_rotation.z -= pi/16
        node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
    elif key == 'h':
        node_rotation.z += pi/16
        node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
    elif key == 't':
        node_rotation.x -= pi/16
        node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
    elif key == 'g':
        node_rotation.x += pi/16
        node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
    elif key == 'r':
        node_rotation.y -= pi/16
        node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
    elif key == 'y':
        node_rotation.y += pi/16
        node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)

    if key == 'u':
        node_scale.x += 0.25
        node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
    elif key == 'j':
        node_scale.x -= 0.25
        node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
    elif key == 'i':
        node_scale.y += 0.25
        node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
    elif key == 'k':
        node_scale.y -= 0.25
        node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
    elif key == 'o':
        node_scale.z += 0.25
        node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
    elif key == 'l':
        node_scale.z -= 0.25
        node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)

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
#
# print("BYPASS")
#
# while True:
#     time.sleep(0.5)
#     print("PING")