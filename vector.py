from math import sqrt

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def from_tuple(tuple):
        return Vec2(tuple[0], tuple[1])

    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ')'

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __div__(self, d):
        d = float(d)
        return Vec2(self.x / d, self.y / d)

    def __mul__(self, a):
        return Vec2(self.x * a, self.y * a)

    def norm(self):
        return sqrt(self.x*self.x + self.y*self.y)

    def norm_square(self):
        return self.x*self.x + self.y*self.y

    def __str__(self):
        return str(self.index)
    index = 0

def dot(v1, v2):
    return v1.x * v2.x + v1.y * v2.y

def cross(v1, v2):
    return v1.x * v2.y - v1.y * v2.x


def to_indices(points):
    indices = []
    for p in points:
        indices.append(p.index)
        pass
    return indices


def to_simple_array(points):
    simple_array = []
    for p in points:
        simple_array.append([p.x, p.y])
        pass
    return simple_array