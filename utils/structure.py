import statistics
from utils.files import read_file

def structure_data(name_file):
	file = read_file(name_file)
	return [convert_to_number(x.split()) for x in file]

def convert_to_number(arr):
	size = len(arr)
	return [float(x) if arr.index(x) < size - 1 else int(x) for x in arr]

def calculate_zscore(data,dimension,quantity):
	quantity = int(quantity)
	for x in range(quantity):
		for y in range(dimension):
			averenge = statistics.mean(data[x])
			dp = statistics.stdev(data[x])
			data[x][y] = (data[x][y] - averenge)/dp
	return data