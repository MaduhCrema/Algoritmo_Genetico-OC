import random
import math
from pip import main
from bin2float import calcBin2Float
from population import calcXBin
from population import calcYBin

# Calculo da função


def calc(a, b):
    fun = (math.sin(a)**3 * math.sin(b))/(a**3 * (a+b))
    return fun


def proximo(lst, K):

    return lst[min(range(len(lst)), key=lambda i: abs(lst[i]-K))]


def roleta(x, tamPop):
    roleta = []
    somatorio = 0
    for i in range(tamPop):
        somatorio += x[i]['Fitness']
    #print("SOMA = ", somatorio)
    # colocando em escala de 0 a 100
    for i in range(tamPop):
        roleta.append(abs((x[i]['Fitness'] * 100) / somatorio))
    #print("roleta = ", roleta)

    # pega um numero entre 0 e 100, e seleciona o numeor mais proximo dele
    sel = random.randrange(0, 100)
    #print("Numero random = ", sel)
    selecionado = proximo(roleta, sel)

    # procura a posição do numero selecionado
    for i in range(tamPop):
        if(roleta[i] == selecionado):
            pos = i

    return selecionado, pos
