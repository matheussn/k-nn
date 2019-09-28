import random
import sys

from accuracy.accuracy import get_accuracy
from utils.knn import get_classification
from utils.makeFolds import make_folds
from utils.structure import structure_data
from utils.distance import calc_distance

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Você precisa informar o arquivo a ser lido!")
        exit(-1)

    k_fold = int(sys.argv[2])
    k_neighbors = int(sys.argv[3])

    hit = 0

    data = structure_data(sys.argv[1])
    [quantity, dimension] = data[0]
    del data[0]
    random.shuffle(data)

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

