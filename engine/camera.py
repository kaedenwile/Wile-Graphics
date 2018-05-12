from algebra import Vec2
from engine.node import Node
from engine.transform import Transform
from algebra.vec3 import Vec3


class Camera(Node):

    def __init__(self, focal_length, width, height, near_depth, far_depth, transform=Transform.none()):
        Node.__init__(self, transform=transform)

        self.focal_length = focal_length
        self.width = width
        self.height = height

        self.near_depth = near_depth
        self.far_depth = far_depth

    def make(self, transform):
        """
        Returns a Vec3 -- the focal point of the camera,
        followed by an array of the four corners of the screen
        in counterclockwise order starting in the upper right,
        all with the transform applied. The fifth is the center.
        A reference to self is also attached.
        """

        w = self.width / 2.0
        h = self.height / 2.0
        f = self.focal_length

        focus = transform.apply(Vec3.zero())
        center = transform.apply(Vec3(0, f, 0))
        focus_to_center = center - focus

        right = (transform.apply(Vec3(w, f, 0)) - center)
        top = (transform.apply(Vec3(0, f, h)) - center)

        def map_to_2d(vector):
            offset = vector - center
            return Vec2(offset.dot(right) / pow(w, 2), offset.dot(top) / pow(h, 2))

        def find_intersect(v):
            # t = (center.y - focus.y) / (v.y - focus.y) if v.y != focus.y else float('NaN')

            # t = (v.y - focus.y) / (center.y - focus.y) if v.y != focus.y else float('NaN')
            focus_to_v = v - focus
            t = focus_to_v.dot(focus_to_center) / focus_to_v.length()
            return focus + (v - focus) * t, t

        return {
            "focus": focus,
            "center": center,
            "camera": self,
            "2d": map_to_2d,
            "intersect": find_intersect,
        }

