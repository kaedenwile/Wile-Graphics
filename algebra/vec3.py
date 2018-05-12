class Vec3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return ( self.x == other.x and self.y == other.y and self.z == other.z)

    @staticmethod
    def zero():
        return Vec3(0, 0, 0)

    def add(self, vec_1, vec_2):
        return Vec3(vec_1.x + vec_2.x, vec_1.y + vec_2.y, vec_1.z + vec_2.z)

    def multiply(self, vec_1, scalar):
        return Vec3(vec_1.x * scalar, vec_1.y * scalar, vec_1.z * scalar)


