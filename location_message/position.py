from mcdreforged.api.utils import Serializable


class Position(Serializable):

    x: float
    y: float
    z: float

    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        return iter((self.x, self.y, self.z))
