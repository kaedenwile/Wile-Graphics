from algebra import Vec3


class Transform:

    def __init__(self, translation, rotation, scaling):
        self.translation = translation
        self.rotation = rotation
        self.scaling = scaling

    def apply(self, vertex):
        pass


    @staticmethod
    def none():
        return Transform(Vec3.zero(), Vec3.zero(), Vec3.zero())
