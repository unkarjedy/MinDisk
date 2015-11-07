import numpy as np
import vector as vec
from vector import Vec2
import generate_vertex_set as gvs
import min_disk as md
import plots as plt
import time
import cProfile
import re
import cProfile, pstats, StringIO
import utils

def main():
    for attemp in range(1000):
        radius = 10
        n = 30
        points = gvs.generate_vertex_set(radius, n)
        points_array = vec.to_simple_array(points)

        disk, disk_points_indices = md.build_min_disk(points)
        print(disk_points_indices)
        print disk
        print

        plt.prepare_axis(radius)

        plt.draw_points(points_array, enumerate = True)
        plt.draw_disk((disk.center.x, disk.center.y, disk.radius))

        plt.draw()



def main_test():
    file = utils.get_file_from_parameters()

    amount = int(file.readline())
    print "samples = ", amount

    time_results = []
    for i in range(amount):
        N = int(file.readline())
        points = np.fromfile(file = file, dtype = int, count = 2 * N, sep=" ").reshape(N, 2)
        vec_points = []
        for i in range(len(points)):
            p = points[i]
            vec_points.append(Vec2(long(p[0]), long(p[1])))


        start_time = time.time()
        disk, disk_points_indices = md.build_min_disk(vec_points)
        end_time = time.time()

        result = (N, end_time - start_time)
        time_results.append(result)
        print result

    print time_results


###################### MAIN #####################
if __name__ == "__main__":
    main()
    # main_test()