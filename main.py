from dataclasses import dataclass
from lib2to3.pytree import convert
import math
import random
from bin2float import calcBin2Float
from population import calcXBin
from population import calcYBin
from genetic import cruzamento
from selecao import roleta
from verificacao import verificaX
from verificacao import verificaY

somatoria = 0.0
# Calculo da função


def calc(a, b):
    fun = (math.sin(a)**3 * math.sin(b))/(a**3 * (a+b))
    return fun


# Criando as populações
Populacao = []
novaPop = []
for i in range(10):
    cromossomo = {'X - Bin': calcXBin(), 'Y - Bin': calcYBin(),
                  'X - Dec': 0.0, 'Y - Dec': 0.0, 'Fitness': 0.0}
    cromossomo['X - Dec'] = calcBin2Float(cromossomo['X - Bin'])
    cromossomo['Y - Dec'] = calcBin2Float(cromossomo['Y - Bin'])
    cromossomo['Fitness'] = calc(cromossomo['X - Dec'], cromossomo['Y - Dec'])
    Populacao.append(cromossomo)
# print(Populacao)

# seleção da roleta
paiX, pos1 = roleta(Populacao, 10)
paiY, pos2 = roleta(Populacao, 10)
print("Pai Aptidão X = ", paiX, "Posição = ", pos1)
print("Pai Aptidão Y = ", paiY, "Posição = ", pos2)
Pai1 = Populacao[pos1]
Pai2 = Populacao[pos2]
# cruzamento de x
# se os filhos fazerm parte da geração seguinte
if(random.uniform(0, 100) <= 85):
    print("CRUZA")
    filho1, filho2 = cruzamento(Pai1, Pai2)

    filho1 = verificaX(filho1)
    filho2 = verificaY(filho2)
    # append
    cromossomo = {'X - Bin': filho1, 'Y - Bin': filho2,
                  'X - Dec': 0.0, 'Y - Dec': 0.0, 'Fitness': 0.0}
    cromossomo['X - Dec'] = calcBin2Float(cromossomo['X - Bin'])
    cromossomo['Y - Dec'] = calcBin2Float(cromossomo['Y - Bin'])
    cromossomo['Fitness'] = calc(cromossomo['X - Dec'], cromossomo['Y - Dec'])
    novaPop.append(cromossomo)
# se os pais fazem parte da geração seguinte
else:
    Pai1 = verificaX(Pai1)
    Pai2 = verificaY(Pai2)
    # append
    cromossomo = {'X - Bin': Pai1, 'Y - Bin': Pai2,
                  'X - Dec': 0.0, 'Y - Dec': 0.0, 'Fitness': 0.0}
    cromossomo['X - Dec'] = calcBin2Float(cromossomo['X - Bin'])
    cromossomo['Y - Dec'] = calcBin2Float(cromossomo['Y - Bin'])
    cromossomo['Fitness'] = calc(cromossomo['X - Dec'], cromossomo['Y - Dec'])
    novaPop.append(cromossomo)

print("-----NOVA POP------")
print(novaPop)
