import matplotlib.pyplot as plt
import numpy as np

def prepare_axis(radius):
    plt.axes([0.025, 0.05, 0.95, 0.95])
    plt.gca().set_aspect('equal', adjustable = 'box')
    border = radius * 1.5
    plt.xlim(-border, border), plt.xticks([])
    plt.ylim(-border, border), plt.yticks([])

    plt.gca().set_xticks(np.arange(-radius, radius + 1, radius / 10))
    plt.gca().set_yticks(np.arange(-radius, radius + 1, radius / 10))
    plt.grid()

def draw_points(points, enumerate = False):
    plt.scatter(zip(*points)[0], zip(*points)[1], s = 10)
    if enumerate:
        shift = 0.2
        for i in range(len(points)):
            plt.annotate(i, (points[i][0] + shift, points[i][1] + shift))

def draw_disk(disk):
    circle = plt.Circle((disk[0], disk[1]), disk[2], color = 'b', fill = False)
    center = plt.Circle((disk[0], disk[1]), 0.1, color = 'r', fill = True)
    plt.gca().add_artist(circle)
    plt.gca().add_artist(center)


def draw():
    plt.show()