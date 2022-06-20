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

def roleta(vetPop, nElementos):
    soma = 0.0
    conta = 0
    vetAptidao = []
    for i in range(nElementos):
        soma += vetPop[i]['Fitness']
    print("Soma = ", soma)

    for i in range(nElementos):
        conta = abs((vetPop[i]['Fitness']* 100)/soma)
        vetAptidao.append(conta)

    #print("-----------Vetor de Aptidão fitness----------")
    #print(vetAptidao)

    for j in range(nElementos):
        random.seed()
        r = random.uniform(0, soma)
        somaT = 0
        i = 0
        while(r >= somaT):
            somaT += vetPop[i]['Fitness']
            i += 1
            if i >= nElementos:
                break
        cromo = vetPop[i-1]['Fitness']
    print("Melhor caso = ", cromo)
    return cromo

