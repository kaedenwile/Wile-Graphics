

class Vec3(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return pow(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2), 0.5)

    def normalized(self):
        return self * (1 / self.length())

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return self + other * -1

    def __mul__(self, other):
        return Vec3(self.x * other, self.y * other, self.z * other)

    def __str__(self):
        return "<%i, %i, %i>" % (self.x, self.y, self.z)

    def __iter__(self):
        return iter([self.x, self.y, self.z])

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vec3(self.y*other.z - self.z*other.y, -self.x*other.z+self.z*other.x, self.x*other.y-self.y*other.x)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    @staticmethod
    def zero():
        return Vec3(0, 0, 0)


