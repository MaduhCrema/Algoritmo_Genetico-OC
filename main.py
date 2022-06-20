import math
from bin2float import calcBin2Float
from population import calcXBin
from population import calcYBin
from genetic import cruzamento
from dataclasses import dataclass

#Calculo da função
def calc(a, b):
    fun = (math.sin(a)**3 * math.sin(b))/(a**3 * (a+b))
    return fun

@dataclass
class Individuo_X:
    x: list
    fitness: float

#Criando as populações
PopX = []
for i in range(10):
    PopX.append(Individuo_X(calcXBin(), 0))

for i in range(10):
    PopX[i].fitness = calc(calcBin2Float(PopX[i].x), 0.001)
    print(PopX[i])
    print("\n")