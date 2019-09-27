

def euclidean_distance(first, second):
    result = sum_lists(first, second)
    result = sum(result)
    return result ** (1/2)


def sum_lists(first, second):
    return [(float(elemA) - float(elemB)) ** 2 for elemA, elemB in zip(first, second)]
	
	
def calc_distance(point, point_list):
	size = len(point)
	return [(euclidean_distance(point, point2),point2[size-1]) for point2 in point_list]
	
	
	

	