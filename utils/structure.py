from utils.files import read_file


def structure_data(name_file):
	file = read_file(name_file)
	return [convert_to_number(x.split()) for x in file]


def convert_to_number(arr):
	size = len(arr)
	return [float(x) if arr.index(x) < size - 1 else int(x) for x in arr]
