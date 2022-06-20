import math
import random

#Função para realizar a mutação
def mutacao(filho):
    #Aplica a mutação no bit de posição 2
    if(filho[2] == 0):
        filho[2] = 1
    else:
        filho[2] = 0

    #Aplica a mutação no bit de posição 6
    if(filho[6] == 0):
        filho[6] = 1
    else:
        filho[6] = 0
    
    return filho

#Função para realizar o cruzamento gentico
def cruzamento(pai1, pai2):
    filho1 = pai1
    filho2 = pai2

    #Realização do cruzamento dos cromossomos dos pais
    for i in range(4):
        filho1[i+2] = pai2[i+2]
        filho2[i+2] = pai1[i+2]
    
    #Realização da mutação dos filhos
    if( random.uniform(0, 100) < 5 ):
        filho1 = mutacao(filho1)
    if( random.uniform(0, 100) < 5 ):
        filho2 = mutacao(filho2)

    return filho1, filho2
