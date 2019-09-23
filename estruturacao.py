import sys


def lerArquivo(arquivo):
	arq = open(arquivo, 'r')
	test = arq.readlines()
	test = [x.split() for x in test]
	del test[0]
	return test

def converteCoord(linhas, lista):
	test1 = []
	for y in range(totalLinhas):
		test1.append([float(x) for x in lista[y]])
	return test1

def dimensao(ponto):
	d = len(ponto)
	return d
	
def agrupamentoPontos(totalLinhas, d, test1):
	test2 = []
	for y in range(totalLinhas):
		for v in range(d):
			teste = test1[y][0:d-1]
			teste.append(int(test1[y][d-1]))
		test2.append(teste)
	return test2

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Você precisa informar o arquivo a ser lido!")
		exit(-1)
	
	test = lerArquivo(sys.argv[1])
	totalLinhas = len(test)
	test1 = converteCoord(totalLinhas, test)
	d = dimensao(test1[0])
	dadosEstruturados = agrupamentoPontos(totalLinhas, d, test1)
	print(dadosEstruturados)
