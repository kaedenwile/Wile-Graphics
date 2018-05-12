class Mat3:

    def __init__(self, values):
        self.values = values

    def __getitem__(self, other):
        return Mat3([

        ])

    @staticmethod
    def zero():
        return Mat3([0, 0, 0,
                     0, 0, 0,
                     0, 0, 0])
