class Vec2(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%i, %i)" % (self.x, self.y)