
def proximo(lst, K):

    return lst[min(range(len(lst)), key=lambda i: abs(lst[i]-K))]


def calcElitismo(Pop, n):
    fitness = 0.13765
    pos = 0
    vetFit = []
    for i in range(0, n):
        vetFit.append(float(Pop[i]['Fitness']))

    selecionado = proximo(vetFit, fitness)
    # procura a posição do numero selecionado
    for i in range(n):
        if(Pop[i]['Fitness'] == selecionado):
            pos = i

    return(selecionado, pos)
