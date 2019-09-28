def euclidean_distance(first, second):
    result = sum_lists(first, second)
    result = sum(result)
    return result ** (1 / 2)


def sum_lists(first, second):
    return [(float(elemA) - float(elemB)) ** 2 for elemA, elemB in zip(first, second)]


def calc_distance(point, point_list):
    size_point = len(point) - 1
    point1 = point[0:size_point]
    return [(euclidean_distance(point1, point2[0:size_point]), point2[size_point]) for point2 in point_list]
