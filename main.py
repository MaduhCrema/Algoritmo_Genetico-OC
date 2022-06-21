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
from elitismo import calcElitismo

# Interface
Geracao = int(input("Quantas gerações você deseja formar?"))
nElementos = int(
    input("Quantos elementos em cada população você deseja gerar?"))

# ----------------------------GERANDO A POPULAÇÃO INICIAL-----------------------------------------------
somatoria = 0.0
# Calculo da função


def calc(a, b):
    fun = (math.sin(a)**3 * math.sin(b))/(a**3 * (a+b))
    return fun


# Criando as populações
Populacao = []
novaPop = []
for i in range(nElementos):
    cromossomo = {'X - Bin': calcXBin(), 'Y - Bin': calcYBin(),
                  'X - Dec': 0.0, 'Y - Dec': 0.0, 'Fitness': 0.0}
    cromossomo['X - Dec'] = calcBin2Float(cromossomo['X - Bin'])
    cromossomo['Y - Dec'] = calcBin2Float(cromossomo['Y - Bin'])
    cromossomo['Fitness'] = calc(cromossomo['X - Dec'], cromossomo['Y - Dec'])
    Populacao.append(cromossomo)
# print(Populacao)
#melhor, posM = calcElitismo(Populacao, nElementos)
j = 0

while(j <= nElementos):
    # seleção da roleta
    paiX, pos1 = roleta(Populacao, nElementos)
    paiY, pos2 = roleta(Populacao, nElementos)
    #print("Pai Aptidão X = ", paiX, "Posição = ", pos1)
    #print("Pai Aptidão Y = ", paiY, "Posição = ", pos2)
    Pai1 = Populacao[pos1]
    Pai2 = Populacao[pos2]

    # CRUZAMENTO E MUTAÇÃO
    # se os filhos fazerm parte da geração seguinte
    if(random.uniform(0, 100) <= 85):
        # print("CRUZA")
        filho1, filho2 = cruzamento(Pai1, Pai2)

        filho1 = verificaX(filho1)
        filho2 = verificaY(filho2)
        # append
        cromossomo = {'X - Bin': filho1, 'Y - Bin': filho2,
                      'X - Dec': 0.0, 'Y - Dec': 0.0, 'Fitness': 0.0}
        cromossomo['X - Dec'] = calcBin2Float(cromossomo['X - Bin'])
        cromossomo['Y - Dec'] = calcBin2Float(cromossomo['Y - Bin'])
        cromossomo['Fitness'] = calc(
            cromossomo['X - Dec'], cromossomo['Y - Dec'])
        novaPop.append(cromossomo)
    # se os pais fazem parte da geração seguinte
    else:
        PaiX2 = Pai1['X - Bin']
        PaiY2 = Pai1['Y - Bin']
        print("PAIS = ", PaiX2, PaiY2)
        # append
        cromossomo = {'X - Bin': PaiX2, 'Y - Bin': PaiY2,
                      'X - Dec': 0.0, 'Y - Dec': 0.0, 'Fitness': 0.0}
        cromossomo['X - Dec'] = calcBin2Float(cromossomo['X - Bin'])
        cromossomo['Y - Dec'] = calcBin2Float(cromossomo['Y - Bin'])
        cromossomo['Fitness'] = calc(
            cromossomo['X - Dec'], cromossomo['Y - Dec'])
        novaPop.append(cromossomo)

    j += 1

print("-----NOVA POP------")
print(novaPop)
# ----------------------------GERANDO OUTRAS POPULAÇÕES-----------------------------
"""cont = 0
while(cont <= Geracao):
    for i in range(1, nElementos):
        cromossomo = {'X - Bin': calcXBin(), 'Y - Bin': calcYBin(),
                      'X - Dec': 0.0, 'Y - Dec': 0.0, 'Fitness': 0.0}
        cromossomo['X - Dec'] = calcBin2Float(cromossomo['X - Bin'])
        cromossomo['Y - Dec'] = calcBin2Float(cromossomo['Y - Bin'])
        cromossomo['Fitness'] = calc(
            cromossomo['X - Dec'], cromossomo['Y - Dec'])
        Populacao.append(cromossomo)"""
