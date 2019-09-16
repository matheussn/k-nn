import sys

from utils.distance import euclidean_distance
from utils.files import read_file

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Você precisa informar o arquivo a ser lido!")
        exit(-1)

    file = read_file(sys.argv[1])
    test = file.readline().split()
    print(euclidean_distance(file.readline().split(), file.readline().split()))
    print(file.readline())
