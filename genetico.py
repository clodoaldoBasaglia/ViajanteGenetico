import copy
import random
import matplotlib.pyplot as plt

def crossover_ordenado(parent1, parent2):
    
    filho = parent1

    #inicia p com numeros aleatorios depois ordena
    p = random.randint(0, len(parent1))
    p.sort()

    s = []

    #cada elemento de p, insere em s o elemento correspondente em p1
    for i in p:
        s.append(parent1[i])

    p_ord = []


    for i in parent2:
        if i in s:
            p_ord.append(s.index(i))

    for i in range(len(s)):
        filho[p[i]] = s[p_ord[i]]

    return filho


def crossover_alternativo(parent1, parent2):
    
    filho = parent1

    # corte aleatoria
    corte = random.randrange(1, len(parent1))

    for i in range(corte, len(parent1)):

        #se parent2[i] esta entre as posicoes 0 e corte do vetor filho
        if (parent2[i] not in filho[0:i]):
            #se não

            # o valor de filho[i] substitui a posicao que tem o valor igual a parent2[i] no vetor filho
            filho[filho.index(parent2[i])] = filho[i]
            
            # agora filho[i] = parent2[i]
            filho[i] = parent2[i]

    return filho

def mutation1(r):

    a = random.randint(0, len(r)-1)
    b = random.randint(0, len(r)-1)

    temp = r[a]
    r[a] = r[b]
    r[b] = temp

    return r

# def mutation2(r):
#     a = random.randint(1, len(r)-1)

#     for i in range(0, len(r)-k, k):
#         temp = r[i]
#         r[i] = r[i+k]
#         r[i+k] = temp

#     return r