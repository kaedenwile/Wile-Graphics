

class Face(object):

    def __init__(self, v1, v2, v3, shader, offset=0):
        self.verts = (v1+offset, v2+offset, v3+offset)
        self.shader = shader

