import random
import sys

from utils.makeFolds import make_folds
from utils.structure import structure_data

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Você precisa informar o arquivo a ser lido!")
        exit(-1)

    k_fold = int(sys.argv[2])
    k_neighbors = int(sys.argv[3])

    data = structure_data(sys.argv[1])
    [quantity, dimension] = data[0]
    del data[0]
    random.shuffle(data)

    fold = make_folds(data, k_fold)

    print(data)
