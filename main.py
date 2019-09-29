import random
import sys

from accuracy.accuracy import get_accuracy
from utils.knn import get_classification
from utils.makeFolds import make_folds
from utils.structure import structure_data,calculate_zscore
from utils.distance import calc_distance

if __name__ == '__main__':
    if len(sys.argv) == 4:
        print("Você precisa informar o nome do arquivo, quantidade de folds, vizinhos e se quer normalizar os dados!")
        exit(-1)

    try:
        k_fold = int(sys.argv[2])
        k_neighbors = int(sys.argv[3])
    except ValueError:
        print("Valore passados para fols e vizinhos inválidos")
        exit(-1)
    
    if not(sys.argv[4].upper() == 'S' or sys.argv[4].upper() == 'N'):
        print("Dados inválidos para normalização.")
        exit(-1)

    hit = 0

    data = structure_data(sys.argv[1])
    [quantity, dimension] = data[0]
    del data[0]
    random.shuffle(data)

    if sys.argv[4].upper() == 'S':
        data = calculate_zscore(data,dimension,quantity)

    fold = make_folds(data, k_fold)
    set_fold = set([tuple(x) for x in data])

    for key in fold.keys():
        test_fold = fold[key]

        set_test_fold = set([tuple(x) for x in test_fold])

        diff = set_fold.difference(set_test_fold)

        for point in test_fold:
            dist = calc_distance(point, diff)

            k = k_neighbors
            while True:
                classification = get_classification(dist, k)

                if classification:
                    break

                k -= 1

            if classification == point[-1]:
                hit += 1

            print(point)
            print(classification)

    print("Taxa de acerto obtido: %f" % get_accuracy(hit, quantity))

