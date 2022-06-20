# Library
import math
import random
from bin2float import calcBin2Float

#Calculo da variavel X para binario
def calcXBin():
    numeroBinX = []
    for i in range(8):
        numero = random.getrandbits(1)
        numeroBinX.append(numero)

    #Para limitar caso ele chegue a 10
    if (numeroBinX[0] == 1):
        numeroBinX[1] = numeroBinX[1] and 0
        numeroBinX[2] = numeroBinX[2] or 0
        numeroBinX[3] = numeroBinX[3] and int(not(numeroBinX[2]))
        for j in range(4):
            numeroBinX[j+4] = 0
    #Se tudo for 0, mudar o ultimo para 1, pois x não aceita 0
    if(numeroBinX == [0, 0, 0, 0, 0, 0, 0, 0]):
        numeroBinX[7] = 1

    return numeroBinX

#Calculo da variavel y para binario
def calcYBin():
    numeroBinY = []
    for i in range(8):
        numero = random.getrandbits(1)
        numeroBinY.append(numero)

    # para limitar caso ele chegue a 10, comparando como uma tabela verdade, quando 1 for ativo o 3 pode ser ativo e o 4 nao, e por assim em diante
    if (numeroBinY[0] == 1):
        numeroBinY[1] = numeroBinY[1] and 0
        numeroBinY[2] = numeroBinY[2] or 0
        numeroBinY[3] = numeroBinY[3] and int(not(numeroBinY[2]))
        for j in range(4):
            numeroBinY[j+4] = 0
    return numeroBinY
