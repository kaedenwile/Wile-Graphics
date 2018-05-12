class Vec3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return ( self.x == other.x && self.y == other.y && self.z == other.z)

    @staticmethod
    def zero():
        return Vec3(0, 0, 0)
