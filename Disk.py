class Disk:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return '((' + str(self.center.x) + ", " + str(self.center.y) + "), " + str(self.radius) + ')'