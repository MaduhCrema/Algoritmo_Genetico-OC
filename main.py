from matplotlib import pyplot as plt
from ctypes import sizeof
from dataclasses import dataclass
from lib2to3.pytree import convert
import math
import random
from numpy import sort
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
# Calculo da função


def calc(a, b):
    fun = (math.sin(a)**3 * math.sin(b))/(a**3 * (a+b))
    return fun


# Criando as populações
Populacao = []
novaPop = []
dados = []
vetMelhorElemento = []
for i in range(nElementos):
    cromossomo = {'X - Bin': calcXBin(), 'Y - Bin': calcYBin(),
                  'X - Dec': 0.0, 'Y - Dec': 0.0, 'Fitness': 0.0}
    cromossomo['X - Dec'] = calcBin2Float(cromossomo['X - Bin'])
    cromossomo['Y - Dec'] = calcBin2Float(cromossomo['Y - Bin'])
    cromossomo['Fitness'] = calc(cromossomo['X - Dec'], cromossomo['Y - Dec'])
    Populacao.append(cromossomo)
# print(Populacao)
# dados utilizados na plotagem do gráfico
for j in range(nElementos):
    dados.append(float(Populacao[j]['Fitness']))

# elitismo de 1 individuo da pop
melhor, posM = calcElitismo(Populacao, nElementos)
# append no vet dos melhores elementos entre as gerações
vetMelhorElemento.append(Populacao[posM])
# coloca a melhor opção na proxima geração(2°)
novaPop.append(Populacao[posM])
# print(Populacao[posM])

j = 0

while(j < nElementos - 1):
    # seleção da roleta
    paiX, pos1 = roleta(Populacao, nElementos)
    paiY, pos2 = roleta(Populacao, nElementos)
    # print("Pai Aptidão X = ", paiX, "Posição = ", pos1)
    # print("Pai Aptidão Y = ", paiY, "Posição = ", pos2)
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
        # print("PAIS = ", PaiX2, PaiY2)
        # append
        cromossomo = {'X - Bin': PaiX2, 'Y - Bin': PaiY2,
                      'X - Dec': 0.0, 'Y - Dec': 0.0, 'Fitness': 0.0}
        cromossomo['X - Dec'] = calcBin2Float(cromossomo['X - Bin'])
        cromossomo['Y - Dec'] = calcBin2Float(cromossomo['Y - Bin'])
        cromossomo['Fitness'] = calc(
            cromossomo['X - Dec'], cromossomo['Y - Dec'])
        novaPop.append(cromossomo)

    j += 1

# print("-----NOVA POPULAÇÃO------")
# print(novaPop)
# dados utilizados na plotagem do gráfico
for j in range(nElementos):
    dados.append(float(novaPop[j]['Fitness']))
# ----------------------------GERANDO OUTRAS POPULAÇÕES-----------------------------
cont = 2
while(cont <= Geracao):
    # vet aux
    aux = []
    # elitismo de 1 individuo da pop
    melhor, posM = calcElitismo(novaPop, nElementos)
    # append no vet dos melhores elementos entre as gerações
    vetMelhorElemento.append(novaPop[posM])
    # reset vetor
    # antes de resetar
    aux = novaPop
    # reseta
    novaPop = []
    # coloca a melhor opção na proxima geração(n°)
    novaPop.append(Populacao[posM])
    # print(Populacao[posM])
    j = 0

    while(j < nElementos - 1):
        # seleção da roleta
        paiX, pos1 = roleta(aux, nElementos)
        paiY, pos2 = roleta(aux, nElementos)
        # print("Pai Aptidão X = ", paiX, "Posição = ", pos1)
        # print("Pai Aptidão Y = ", paiY, "Posição = ", pos2)
        Pai1 = aux[pos1]
        Pai2 = aux[pos2]

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
            # print("PAIS = ", PaiX2, PaiY2)
            # append
            cromossomo = {'X - Bin': PaiX2, 'Y - Bin': PaiY2,
                          'X - Dec': 0.0, 'Y - Dec': 0.0, 'Fitness': 0.0}
            cromossomo['X - Dec'] = calcBin2Float(cromossomo['X - Bin'])
            cromossomo['Y - Dec'] = calcBin2Float(cromossomo['Y - Bin'])
            cromossomo['Fitness'] = calc(
                cromossomo['X - Dec'], cromossomo['Y - Dec'])
            novaPop.append(cromossomo)

        j += 1

    cont += 1
    # dados utilizados na plotagem do gráfico
    for j in range(nElementos):
        dados.append(float(novaPop[j]['Fitness']))
    # print("-----NOVA POPULAÇÃO------")
    # print(novaPop)
print("-----------MELHORES ELEMENTOS----------")
print(vetMelhorElemento)
print("-----------MELHOR FITNESS----------")
melhorElemento, posE = calcElitismo(vetMelhorElemento, Geracao)
print(melhorElemento)

# plotagem de gráfico
plt.plot(range(len(dados)), sort(dados))
plt.grid(True, zorder=0)
plt.title("Elitismo do fitness")
plt.xlabel("Quantidade de Fitness")
plt.ylabel("Valor do fitness")
plt.show()
