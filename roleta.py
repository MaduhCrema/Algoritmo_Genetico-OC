import random


def roleta(vet, nElementos):
    soma = 0
    conta = 0
    vetAptidao = []
    for i in range(nElementos):
        soma += vet[i].fitness
    print("Soma = ", soma)

    for i in range(nElementos):
        conta = abs((vet[i].fitness * 100)/soma)
        vetAptidao.append(conta)

    print("-----------Vetor de Aptidão fitness----------")
    print(vetAptidao)

    for i in range(nElementos):
        r = random.uniform(0, soma)
        somaT = 0
        i = 0
        while(somaT < soma):
            somaT += vet[i].fitness
            i += 1
        cromo = vet[i-1].fitness
    print("Melhor caso = ", cromo)
    return cromo
