import statistics
from utils.files import read_file


def structure_data(name_file):
	file = read_file(name_file)
	return [convert_to_number(x.split()) for x in file]


def convert_to_number(arr):
	size = len(arr)
	return [float(x) if arr.index(x) < size - 1 else int(x) for x in arr]


def calculate_z_score(data, dimension, quantity):
	average = []
	dp = []
	quantity = int(quantity)
	for x in range(dimension):
		columns = list(row[x] for row in data)
		average.append(sum(columns)/quantity)
		dp.append(statistics.stdev(columns))

	for y in range(quantity):
		for x in range(dimension):
			data[y][x] = (data[y][x] - average[x])/dp[x]
	return data
