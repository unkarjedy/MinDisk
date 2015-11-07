from copy import copy
import random
import vector as vec
from vector import Vec2
from Disk import Disk

# Builds min disk from points
# returns center and radius of mindisk
# returns indices of mindisk points
def build_min_disk(points):
    disk_points = min_disk(points)
    disk = build_disk_from_points(disk_points)
    disk_points_indices = vec.to_indices(disk_points)
    return disk, disk_points_indices


# returns indices of mindisk points
def min_disk(points):
    points_len = len(points)
    if points_len < 2:
        return None
    else:
        return min_disk_recursive(points[:])


# params:
#   points - array of points to build min disk on (~{ p })
#   fixed - points that are known they lay on the min disk of 'points' (~ q1, q2)
def min_disk_recursive(points, fixed = []):
    fixed_len = len(fixed)
    if fixed_len == 3:
        return fixed[:]

    random.shuffle(points)

    D = []
    for i in range(fixed_len):
        D.append(fixed[i])
    for i in range(2 - fixed_len):
        D.append(points[i])

    for i in range(2 - fixed_len, len(points)):
        if not is_in_disk(points[i], D):
            D = min_disk_recursive(points[:i], fixed + [points[i]])

    return D


def square2(p1, p2, p3):
    return vec.cross(p2 - p1, p3 - p1)


def getD_DX_DY(p1, p2, p3):
    D = 2 * square2(p1, p2, p3)

    r1 = p1.norm_square()
    r2 = p2.norm_square()
    r3 = p3.norm_square()

    p1copy = copy(p1)
    p2copy = copy(p2)
    p3copy = copy(p3)

    p1copy.x = r1
    p2copy.x = r2
    p3copy.x = r3

    DX = square2(p1copy, p2copy, p3copy)

    p1copy.y = p1.x
    p2copy.y = p2.x
    p3copy.y = p3.x

    DY = square2(p1copy, p2copy, p3copy)

    return long(D), long(DX), long(DY)


# return center and radius of disk by its (2-3) points
def build_disk_from_points(points):
    disk_points_len = len(points)
    if disk_points_len < 2 or disk_points_len > 3:
        return

    p1 = points[0]
    p2 = points[1]

    if disk_points_len == 2:
        center = (p2 + p1) / 2
        return Disk(center, (p2 - center).norm())

    p3 = points[2]
    D, DX, DY = getD_DX_DY(p1, p2, p3)

    center = Vec2(DX, -DY) / D
    return Disk(center, (p1 - center).norm())


def is_in_disk(q, Disk):
    p1 = Disk[0]
    p2 = Disk[1]

    if len(Disk) == 2:
        c2 = p1 + p2
        rad_vec = p1 * 2 - c2
        dist_vec = q * 2 - c2
        return vec.dot(dist_vec, dist_vec) <= vec.dot(rad_vec, rad_vec)

    if len(Disk) == 3:
        p3 = Disk[2]
        D, DX, DY = getD_DX_DY(p1, p2, p3)
        return ((D * q.x - DX) ** 2 + (D * q.y + DY) ** 2) <= ((D * p1.x - DX) ** 2 + (D * p1.y + DY) ** 2)

    return False