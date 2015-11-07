import numpy as np
import math
from vector import Vec2


def generate_vertex_set(radius = 10, n = 1024):

    A = np.random.uniform(-math.pi, math.pi, n)
    R = np.random.uniform(0, radius, n)
    points = []
    for id in range(n):
        points.append(Vec2(long(math.floor(R[id] * math.cos(A[id]))),
                 long(math.floor(R[id] * math.sin(A[id])))))
        points[id].index = id

    return points


def generate_geometric_to_file(filename, amount, start_N, multiply):
    outfile = file(filename, 'w')

    outfile.write('{0}\n'.format(amount))

    N = start_N
    for i in range(amount):
        outfile.write('{0}\n'.format(N))

        points = generate_vertex_set(radius = amount,
                                     n = N )
        np.savetxt(outfile, points, fmt = '%d')

        N *= multiply;



if __name__ == "__main__":
    generate_geometric_to_file(filename = 'samples.txt',
                           amount = 10,
                           start_N = 20,
                           multiply = 2);

