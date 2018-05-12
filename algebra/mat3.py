from algebra import Vec3


class Mat3:

    def __init__(self, values):
        self.values = values

    def __getitem__(self, key):
        return self.values[key[0]*3+key[1]]

    def __mul__(self, other):
        if type(other) is Mat3:
            return Mat3([
                self[(0, 0)] * other[(0, 0)] + self[(0, 1)] * other[(1, 0)] + self[(0, 2)] * other[(2, 0)],
                self[(0, 0)] * other[(0, 1)] + self[(0, 1)] * other[(1, 1)] + self[(0, 2)] * other[(2, 1)],
                self[(0, 0)] * other[(0, 2)] + self[(0, 1)] * other[(1, 2)] + self[(0, 2)] * other[(2, 2)],

                self[(1, 0)] * other[(0, 0)] + self[(1, 1)] * other[(1, 0)] + self[(1, 2)] * other[(2, 0)],
                self[(1, 0)] * other[(0, 1)] + self[(1, 1)] * other[(1, 1)] + self[(1, 2)] * other[(2, 1)],
                self[(1, 0)] * other[(0, 2)] + self[(1, 1)] * other[(1, 2)] + self[(1, 2)] * other[(2, 2)],

                self[(2, 0)] * other[(0, 0)] + self[(2, 1)] * other[(1, 0)] + self[(2, 2)] * other[(2, 0)],
                self[(2, 0)] * other[(0, 1)] + self[(2, 1)] * other[(1, 1)] + self[(2, 2)] * other[(2, 1)],
                self[(2, 0)] * other[(0, 2)] + self[(2, 1)] * other[(1, 2)] + self[(2, 2)] * other[(2, 2)],
            ])
        elif type(other) is Vec3:
            return Vec3(
                self[(0, 0)] * other.x + self[(0, 1)] * other.y + self[(0, 2)] * other.z,
                self[(1, 0)] * other.x + self[(1, 1)] * other.y + self[(1, 2)] * other.z,
                self[(2, 0)] * other.x + self[(2, 1)] * other.y + self[(2, 2)] * other.z,
            )

    def __str__(self):
        return "[%i, %i, %i,\n %i, %i, %i,\n %i, %i, %i]" % tuple(self.values)

    @staticmethod
    def zero():
        return Mat3([0, 0, 0,
                     0, 0, 0,
                     0, 0, 0])
