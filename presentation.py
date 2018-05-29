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
sky = Node(sky_mesh, Transform.make(Vec3(0, 30, 0), Vec3.zero(), Vec3(100, 1, 100)), Shader((183, 221, 255)))
scene.root.add_child(sky)


# GROUND

a = Shader((127, 173, 90))
b = Shader((122, 171, 96))
c = Shader((117, 163, 92))
d = Shader((106, 155, 87))
e = Shader((98, 150, 81))
f = Shader((95, 143, 79))
g = Shader((92, 138, 80))
h = Shader((86, 134, 73))

b_l = Shader((124, 171, 97))
c_l = Shader((121, 168, 93))
d_l = Shader((109, 161, 89))
e_l = Shader((100, 155, 83))
f_l = Shader((100, 150, 82))
g_l = Shader((98, 145, 84))

gp = [
    Vec3(0, 0, 0),
    Vec3(0.3, 0, 0),
    Vec3(0.6, 0, 0),
    Vec3(0.6, 0.5, 0),
    Vec3(0.6, 1, 0),
    Vec3(0.3, 1, 0),
    Vec3(0, 1, 0),
    Vec3(0, 0.5, 0),

    Vec3(0.15, 0.15, 0.1),
    Vec3(0.3, 0.15, 0.1),
    Vec3(0.45, 0.15, 0.1),
    Vec3(0.5, 0.4, 0.1),
    Vec3(0.5, 0.6, 0.1),
    Vec3(0.45, 0.7, 0.1),
    Vec3(0.3, 0.75, 0.1),
    Vec3(0.15, 0.7, 0.1),
    Vec3(0.1, 0.6, 0.1),
    Vec3(0.1, 0.4, 0.1),

    Vec3(0.25, 0.35, 0.15),
    Vec3(0.35, 0.35, 0.15),
    Vec3(0.35, 0.45, 0.15),
    Vec3(0.25, 0.45, 0.15),
]

ground_meshes = [
    [0, 1, 8],
    [1, 2, 10],
    [2, 3, 11],
    [3, 4, 12],
    [4, 5, 13],
    [5, 6, 15],
    [6, 7, 16],
    [7, 0, 17],
    [1, 9, 8],
    [1, 10, 9],
    [2, 11, 10],
    [3, 12, 11],
    [4, 13, 12],
    [5, 14, 13],
    [5, 15, 14],
    [6, 16, 15],
    [7, 17, 16],
    [0, 8, 17],
    [8, 9, 18],
    [9, 10, 19],
    [10, 11, 19],
    [11, 12, 20],
    [12, 13, 20],
    [13, 14, 20],
    [14, 15, 21],
    [15, 16, 21],
    [16, 17, 21],
    [17, 8, 18],
    [9, 19, 18],
    [11, 19, 20],
    [14, 21, 20],
    [17, 18, 21],
    [18, 19, 21],
    [19, 20, 21]
]

ground_colors = [
    b_l,
    b_l,
    d,
    f_l,
    f,
    f,
    f_l,
    d,
    a,
    a,
    c_l,
    e,
    g_l,
    g_l,
    g_l,
    g_l,
    e,
    c_l,
    b_l,
    b_l,
    c,
    e_l,
    f,
    g,
    g,
    f,
    e_l,
    c,
    b,
    d_l,
    h,
    d_l,
    c,
    c,
]

ground_node = Node(Mesh.empty(), Transform.make(Vec3(-6, 10, -3), Vec3.zero(), Vec3(20, 20, 20)), Shader((255, 255, 255)))

def create_ground_node():
    for i, m in enumerate(ground_meshes):
        mesh = Mesh([gp[m[0]], gp[m[1]], gp[m[2]]], [(0, 1, 2)])
        n = Node(mesh, Transform.none(), ground_colors[i])
        ground_node.add_child(n)


scene.root.add_child(ground_node)
create_ground_node()



#TRUNK

ta = Shader((210, 184, 106))
tb = Shader((202, 175, 96))
tc = Shader((194, 167, 89))
td = Shader((191, 160, 86))
te = Shader((186, 155, 81))
tf = Shader((181, 149, 75))
tg = Shader((176, 144, 70))

tkp = [
    Vec3(0.05, 0.01, 0),
    Vec3(0.08, 0.05, 0),
    Vec3(0.03, 0.09, 0),
    Vec3(0.06, 0.01, 0.15),
    Vec3(0.06, 0.06, 0.15),
    Vec3(0.01, 0.05, 0.15),
    Vec3(0.07, 0.03, 0.3),
    Vec3(0.05, 0.09, 0.3),
    Vec3(0.02, 0.05, 0.3),
]

trunk_meshes = [
    [0, 1, 3],
    [1, 3, 4],
    [1, 2, 4],
    [2, 4, 5],
    [0, 2, 5],
    [0, 3, 5],
    [3, 6, 8],
    [3, 4, 6],
    [4, 5, 7],
    [5, 8, 7],
    [5, 3, 8]
]

trunk_colors = [
    ta,
    tb,
    td,
    tf,
    tc,
    tb,

    tf,
    tc,
    te,
    tf,
    te,
    tc,
]

tree_node = Node(Mesh.empty(), Transform.make(Vec3(5.5, 7.5, 3), Vec3.zero(), Vec3(0.5, 0.5, 0.7)), Shader((255, 255, 255)))

def create_tree_node():
    for i, m in enumerate(trunk_meshes):
        mesh = Mesh([tkp[m[0]], tkp[m[1]], tkp[m[2]]], [(0, 1, 2)])
        n = Node(mesh, Transform.none(), trunk_colors[i])
        tree_node.add_child(n)

create_tree_node()
ground_node.add_child(tree_node)



#FOLIAGE

fa = Shader((232, 162, 200))
fb = Shader((227, 153, 192))
fc = Shader((222, 144, 185))
fd = Shader((219, 140, 181))
fe = Shader((217, 134, 177))
ff = Shader((212, 127, 171))
fg = Shader((204, 120, 164))
fh = Shader((196, 107, 160))

fp = [
    Vec3(0, 0, 0),
    Vec3(0.2, -0.03, 0.02),
    Vec3(0.18, 0.15, -0.01),
    Vec3(0.02, 0.14, 0),
    Vec3(-0.03, -0.05, 0.25),
    Vec3(0.24, -0.02, 0.26),
    Vec3(0.25, 0.18, 0.25),
    Vec3(-0.05, 0.18, 26),
    Vec3(0.08, 0.08, 0.4),
    Vec3(0.12, 0.07, 0.41),
    Vec3(0.13, 0.14, 0.4),
    Vec3(0.07, 0.14, 0.4),
]

foliage_meshes = [
    [0, 1, 2],
    [0, 2, 3],
    [0, 1, 5],
    [0, 5, 4],
    [1, 5, 6],
    [1, 2, 6],
    [2, 6, 7],
    [2, 3, 7],
    [3, 4, 7],
    [0, 3, 4],
    [4, 5, 9],
    [4, 8, 9],
    [5, 6, 9],
    [6, 9, 10],
    [6, 10, 11],
    [6, 7, 11],
    [7, 8, 11],
    [7, 4, 11],
    [7, 4, 8],
    [8, 9, 11],
    [11, 9, 10]
]

foliage_colors = [
    fh,
    fh,
    fc,
    fb,
    fc,
    fd,
    fe,
    ff,
    fe,
    fc,
    fa,
    fb,
    fc,
    fd,
    fe,
    ff,
    fe,
    fd,
    fc,
    fb,
    fc,
]

foliage_node = Node(Mesh.empty(), Transform.make(Vec3(-0.5, 0, 4), Vec3.zero(), Vec3(1, 1, 1)), Shader((255, 255, 255)))

def create_foliage_node():
    for i, m in enumerate(foliage_meshes):
        mesh = Mesh([fp[m[0]], fp[m[1]], fp[m[2]]], [(0, 1, 2)])
        n = Node(mesh, Transform.none(), foliage_colors[i])
        foliage_node.add_child(n)

create_foliage_node()
tree_node.add_child(foliage_node)

cam_rot = Vec3(0, 0, 0)

camera = Camera(2, 4, 3, 5, 100)
camera.transform.translation.y = -2
camera.transform.translation.z = 3

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
    elif key == 'z':
        camera.transform.translation.z += 1
    elif key == 'x':
        camera.transform.translation.z -= 1
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