# Library
import math
import random

# calculo da função
def calc(a, b):
    fun = (math.sin(a)*3 * math.sin(b))/(a*3 * (a+b))
    return fun


# calculo da variavel x para binario
def calcXBin():
    numeroBinX = []
    for i in range(8):
        numero = random.getrandbits(1)
        numeroBinX.append(numero)

    # para limitar caso ele chegue a 10
    if (numeroBinX[0] == 1):
        numeroBinX[1] = numeroBinX[1] and 0
        numeroBinX[2] = numeroBinX[2] or 0
        numeroBinX[3] = numeroBinX[3] and int(not(numeroBinX[2]))
        for j in range(4):
            numeroBinX[j+4] = 0
    # se tudo for 0, mudar o ultimo para 1, pois x não aceita 0
    if(numeroBinX == [0, 0, 0, 0, 0, 0, 0, 0]):
        numeroBinX[7] = 1

    print(numeroBinX)
    return numeroBinX

# calculo da variavel y para binario


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

    print(numeroBinY)
    return numeroBinY


def calcBin2Float(numeroBin):
    parteInt = []
    parteDec = []
    # separa a parte inteira e a parte fracionária
    for i in range(4):
        parteInt.append(numeroBin[i])
    for j in range(4, 8):
        parteDec.append(numeroBin[j])

    print("Parte Int:", parteInt)
    print("Parte Dec:", parteDec)

    numDec2 = 0.0
    # convertendo para decimal, a parte inteira

    numDec = parteInt[3] + parteInt[2]*2 + parteInt[1]*4 + parteInt[0]*8
    # convertendo para decimal, a parte fracionária
    numDec2 = 0.0
    for i in range(4):
        numDec2 += parteDec[i]/2**(i+1)

    print(numDec)
    print(numDec2)
    # concatenação da parte inteira com a fracionaria
    numero = numDec + numDec2
    print(numero)

# repetindo uma população
for i in range(5):
    print("Passo:", i)
    print("X:")
    numX = calcXBin()
    calcBin2Float(numX)
    numY = calcYBin()
    print("Y:")
    calcBin2Float(numY)
    print("\n")