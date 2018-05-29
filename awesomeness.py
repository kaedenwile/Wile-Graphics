import display
from algebra import Vec3, Mat3
from engine import *
from math import pi

size = width, height = 1280, 960

scene = Scene()

# SKY
sky_mesh = Mesh([
    Vec3(1, 0, 1),
    Vec3(1, 0, -1),
    Vec3(-1, 0, -1),
    Vec3(-1, 0, 1)
], [
    (0, 1, 2),
    (0, 2, 3)
])
sky = Node(sky_mesh, Transform.make(Vec3(0, 30, 0), Vec3.zero(), Vec3(100, 1, 100)), Shader((100, 150, 255)))
scene.root.add_child(sky)


# GROUND
ground_mesh = Mesh([
    Vec3(0, 1, 0),
    Vec3(0.5, 0.866, 0),
    Vec3(0.866, 0.5, 0),
    Vec3(1, 0, 0),
    Vec3(0.866, -0.5, 0),
    Vec3(0.5, -0.866, 0),
    Vec3(0, -1, 0),
    Vec3(-0.5, -0.866, 0),
    Vec3(-0.866, -0.5, 0),
    Vec3(-1, 0, 0),
    Vec3(-0.866, 0.5, 0),
    Vec3(-0.5, 0.866, 0),

    Vec3(0, 0.35, 0.71),
    Vec3(0.25, 0.25, 0.71),
    Vec3(0.35, 0, 0.71),
    Vec3(0.25, -0.25, 0.71),
    Vec3(0, -0.35, 0.71),
    Vec3(-0.25, -0.25, 0.71),
    Vec3(-0.35, 0, 0.71),
    Vec3(-0.25, 0.25, 0.71),

    Vec3(0, 0, .866),
], [
    (0, 12, 1),
    (12, 1, 13),
    (1, 13, 2),
    (13, 14, 2),
    (2, 14, 3),

    (3, 14, 4),
    (14, 15, 4),
    (4, 15, 5),
    (15, 16, 5),
    (5, 16, 6),

    (6, 16, 7),
    (16, 17, 7),
    (7, 17, 8),
    (17, 18, 8),
    (8, 18, 9),

    (9, 18, 10),
    (18, 19, 10),
    (10, 19, 11),
    (19, 12, 11),
    (11, 0, 12),

    (12, 13, 20),
    (13, 14, 20),
    (14, 15, 20),
    (15, 16, 20),
    (16, 17, 20),
    (17, 18, 20),
    (18, 19, 20)
])
ground = Node(ground_mesh, Transform.make(Vec3(0, 10, -6), Vec3.zero(), Vec3(8, 8, 5)), Shader((150, 255, 100)))
scene.root.add_child(ground)

# DUDE
cube = Mesh([
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
dude = Node(cube, Transform.make(Vec3(0, 10, -0), Vec3.zero(), Vec3(1, 1, 1)), Shader((223, 45, 167)))

l_leg = Node(cube, Transform.make(Vec3(0.75, 0, -1.5), Vec3.zero(), Vec3(0.25, 0.25, 0.5)), Shader((124, 23, 255)))
dude.add_child(l_leg)

r_leg = Node(cube, Transform.make(Vec3(-0.75, 0, -1.5), Vec3.zero(), Vec3(0.25, 0.25, 0.5)), Shader((124, 23, 255)))
dude.add_child(r_leg)

l_arm = Node(cube, Transform.make(Vec3(1.5, 0, 0), Vec3.zero(), Vec3(0.5, 0.25, 0.25)), Shader((124, 23, 255)))
dude.add_child(l_arm)

r_arm = Node(cube, Transform.make(Vec3(-1.5, 0, 0), Vec3.zero(), Vec3(0.5, 0.25, 0.25)), Shader((124, 23, 255)))
dude.add_child(r_arm)

r_eye = Node(cube, Transform.make(Vec3(0.4, -1.5, 0.25), Vec3.zero(), Vec3(0.25, 0.125, 0.25)), Shader((124, 23, 255)))
r_pupil = Node(cube, Transform.make(Vec3(0, -0.125, 0), Vec3(0, pi/4, 0), Vec3(0.25, 0.25, 0.25)), Shader((255, 255, 255)))
r_eye.add_child(r_pupil)
dude.add_child(r_eye)

l_eye = Node(cube, Transform.make(Vec3(-0.4, -1.5, 0.25), Vec3.zero(), Vec3(0.25, 0.125, 0.25)), Shader((124, 23, 255)))
l_pupil = Node(cube, Transform.make(Vec3(0, -0.125, 0), Vec3(0, pi/4, 0), Vec3(0.25, 0.25, 0.25)), Shader((255, 255, 255)))
l_eye.add_child(l_pupil)
dude.add_child(l_eye)

mouth_mesh = Mesh([
    Vec3(1, 1, 1),
    Vec3(0, 1, 0.66),
    Vec3(-1, 1, 1),
    Vec3(0, 1, -1),
    Vec3(1, -1, 1),
    Vec3(0, -1, 0.66),
    Vec3(-1, -1, 1),
    Vec3(0, -1, -1),
], [
    (0, 1, 3),
    (1, 2, 3),

    (4, 5, 7),
    (5, 6, 7),

    (0, 4, 1),
    (1, 4, 5),
    (1, 2, 6),
    (1, 5, 6),
    (2, 3, 6),
    (2, 6, 7),
    (7, 4, 3),
    (3, 0, 4)
])
mouth = Node(mouth_mesh, Transform.make(Vec3(0, -1.5, -0.5), Vec3.zero(), Vec3(0.5, 0.125, 0.125)), Shader((255, 255, 255)))
dude.add_child(mouth)

scene.root.add_child(dude)

cam_rot = Vec3(0, 0, 0)

camera = Camera(2, 4, 3, 5, 100)
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
        camera.transform.translation.x -= 1
    elif key == 'd':
        camera.transform.translation.x += 1
    elif key == 'w':
        camera.transform.translation.y += 1
    elif key == 's':
        camera.transform.translation.y -= 1
    elif key == 'q':
        cam_rot.z += pi/16
        camera.transform = Transform.make(camera.transform.translation, cam_rot, Vec3(1, 1, 1))
    elif key == 'e':
        cam_rot.z -= pi/16
        camera.transform = Transform.make(camera.transform.translation, cam_rot, Vec3(1, 1, 1))

    should_draw = True

#     if key == 'f':
#         node_rotation.z -= pi/16
#         node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
#     elif key == 'h':
#         node_rotation.z += pi/16
#         node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
#     elif key == 't':
#         node_rotation.x -= pi/16
#         node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
#     elif key == 'g':
#         node_rotation.x += pi/16
#         node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
#     elif key == 'r':
#         node_rotation.y -= pi/16
#         node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
#     elif key == 'y':
#         node_rotation.y += pi/16
#         node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
#
#     if key == 'u':
#         node_scale.x += 0.25
#         node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
#     elif key == 'j':
#         node_scale.x -= 0.25
#         node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
#     elif key == 'i':
#         node_scale.y += 0.25
#         node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
#     elif key == 'k':
#         node_scale.y -= 0.25
#         node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
#     elif key == 'o':
#         node_scale.z += 0.25
#         node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
#     elif key == 'l':
#         node_scale.z -= 0.25
#         node.transform = Transform.make(node.transform.translation, node_rotation, node_scale)
#
#     elif key == 'z':
#         camera.focal_length *= 0.5
#         # print(camera.focal_length)
#     elif key == 'x':
#         camera.focal_length *= 2
#         # print(camera.focal_length)

display.Screen(*size, title="UW Graphics", frame_rate=60, update=main_loop, callback=key_handler)