import math
from bin2float import calcBin2Float
from population import calcXBin
from population import calcYBin

#Calculo da função
def calc(a, b):
    fun = (math.sin(a)**3 * math.sin(b))/(a**3 * (a+b))
    return fun

#Criando as populações
PopX = []
for i in range(100):
    PopX.append(calcXBin())

PopY = []
for i in range(100):
    PopY.append(calcYBin())
