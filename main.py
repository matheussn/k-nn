import sys

from utils.structure import structure_data

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Você precisa informar o arquivo a ser lido!")
        exit(-1)

    data = structure_data(sys.argv[1])
    [quantity, dimension] = data[0]
    del data[0]

    print(quantity)
    print(dimension)

    print(data)
