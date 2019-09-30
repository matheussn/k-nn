# Arquivos com funções de manipulação de arquivos


def read_file(name):
    file = open(name, mode='r')
    lines = file.readlines()
    file.close()
    return lines
