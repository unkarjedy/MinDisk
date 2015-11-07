from vector import Vec2
import fileinput
import min_disk as md


def get_points_array_from_stdin():
    N = input()
    points = []
    for i in range(N):
        array = map(int, raw_input().split())
        p = [array[0], array[1]]
        points.append(p)

    return points


if __name__ == "__main__":
    points = []

    samples_amount = input()
    for id in range(samples_amount):
        points = get_points_array_from_stdin()
        disk, indices = md.build_min_disk(points)
        print disk
        print indices


