import sys


def lerArquivo(arquivo):
	arq = open(arquivo, 'r')
	test = arq.readlines()
	test = [ x.split() for x in test]
	lista = test[0]
	del test[0]
	return [lista, test]

def converteCoord(lista):
	test1 = []

	for y in range(lista[0][0]):
		test1.append([float(x) for x in lista[1][y]])
		test1[y][lista[0][1]] = int(lista[1][y][lista[0][1]])
	lista[1] = test1
	return lista

def dimensao(lista):
	lista[0][0] = int(lista[0][0])
	lista[0][1] = int(lista[0][1])
	return lista
	

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Você precisa informar o arquivo a ser lido!")
		exit(-1)
	
	test = lerArquivo(sys.argv[1])
	test = dimensao(test)
	test = converteCoord(test)
	
	print(test)
