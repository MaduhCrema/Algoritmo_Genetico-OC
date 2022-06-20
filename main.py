from dataclasses import dataclass
import math
from bin2float import calcBin2Float
from population import calcXBin
from population import calcYBin
from genetic import cruzamento
from selecao import roleta


somatoria = 0.0
# Calculo da função
def calc(a, b):
    fun = (math.sin(a)**3 * math.sin(b))/(a**3 * (a+b))
    return fun

"""@dataclass
class Individuo:
    x: list
    y: list
    fitness: float
"""


# Criando as populações
Populacao= []
for i in range(10):
    cromossomo = {'X - Bin': calcXBin(), 'Y - Bin': calcYBin(), 'X - Dec': 0.0, 'Y - Dec': 0.0, 'Fitness': 0.0, 'Aptidao': 0.0}
    cromossomo['X - Dec'] = calcBin2Float(cromossomo['X - Bin'])
    cromossomo['Y - Dec'] = calcBin2Float(cromossomo['Y - Bin'])
    cromossomo['Fitness'] = calc(cromossomo['X - Dec'], cromossomo['Y - Dec'])
    somatoria += cromossomo['Fitness']
    Populacao.append(cromossomo)

paiX = roleta(Populacao, 10)
paiY = roleta(Populacao, 10)
print("Pai X = ", paiX)
print("Pai Y = ", paiY)
# cruzamento de x


