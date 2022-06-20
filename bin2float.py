import math


def calcBin2Float(numeroBin):
    parteInt = []
    parteDec = []
    # separa a parte inteira e a parte fracionária
    for i in range(4):
        parteInt.append(numeroBin[i])
    for j in range(4, 8):
        parteDec.append(numeroBin[j])

    #print("Parte Int:", parteInt)
    #print("Parte Dec:", parteDec)

    numDec2 = 0.0
    # convertendo para decimal, a parte inteira

    numDec = parteInt[3] + parteInt[2]*2 + parteInt[1]*4 + parteInt[0]*8
    # convertendo para decimal, a parte fracionária
    numDec2 = 0.0
    for i in range(4):
        numDec2 += parteDec[i]/2**(i+1)

    # print(numDec)
    # print(numDec2)
    # concatenação da parte inteira com a fracionaria
    numero = numDec + numDec2
    # print(numero)
    return numero
