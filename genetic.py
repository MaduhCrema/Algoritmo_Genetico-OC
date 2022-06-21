import math
import random

# Função para realizar a mutação do filho 1


def mutacao(filho):

    for i in range(8):
        if(random.uniform(0, 100) <= 75):
            if(filho[i] == 0):
                filho[i] = 1
            else:
                filho[i] = 0
    return filho

# Função para realizar o cruzamento gentico


def cruzamento(p1, p2):
    filho1 = p1['X - Bin']
    filho2 = p2['Y - Bin']
    pai1 = p1['X - Bin']
    pai2 = p2['Y - Bin']
    # Realização do cruzamento dos cromossomos dos pais
    for i in range(2, 5):
        filho1[i] = pai2[i]
    for i in range(1, 2):
        filho2[i] = pai1[i]
    for i in range(5, 8):
        filho2[i] = pai1[i]

    # Realização da mutação dos filhos
    filho1 = mutacao(filho1)
    filho2 = mutacao(filho2)

    print(filho1, filho2)
    return filho1, filho2
