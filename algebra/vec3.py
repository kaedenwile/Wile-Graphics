class Vec3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def zero():
        return Vec3(0, 0, 0)
