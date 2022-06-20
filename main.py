from dataclasses import dataclass
import math
from bin2float import calcBin2Float
from population import calcXBin
from population import calcYBin
from genetic import cruzamento
from roleta import roleta

# Calculo da função


def calc(a, b):
    fun = (math.sin(a)**3 * math.sin(b))/(a**3 * (a+b))
    return fun


@dataclass
class Individuo:
    x: list
    y: list
    fitness: float


# Criando as populações de X
PopX = []
for i in range(10):
    PopX.append(Individuo(calcXBin(), 0, 0))

# Criando as populações de Y
PopY = []
for i in range(10):
    PopY.append(Individuo(0, calcXBin(), 0))
# calculo fitness
for i in range(10):
    PopX[i].fitness = calc(calcBin2Float(PopX[i].x), 0.01)
    PopY[i].fitness = calc(0.0001, calcBin2Float(PopY[i].y))
    print(PopX[i])
    print(calcBin2Float(PopX[i].x))
    print(PopY[i])
    print(calcBin2Float(PopY[i].y))
    print("\n")
# calculo roleta
vetAptidao = []
melhorX = roleta(PopX, 10)
melhorY = roleta(PopY, 10)
