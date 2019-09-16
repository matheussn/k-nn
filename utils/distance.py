

def euclidean_distance(first, second):
    result = sum_lists(first, second)
    result = sum(result)
    return result ** (1/2)


def sum_lists(first, second):
    return [(float(elemA) - float(elemB)) ** 2 for elemA, elemB in zip(first, second)]