import random
import matplotlib.pyplot as plt
import math

def crossover_ordered(parent1, parent2):
    
    son = parent1
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
        son[p[i]] = s[p_ord[i]]

    return son


def crossover_alternative(parent1, parent2):
    
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

def generate_population(size, dimension):
    list_cities = range(1, dimension+1)
    r = random.sample(list_cities, dimension)

    population = []
    for i in range(size):
        population.append(r)
    return population

def fitness(vector, matriz_distance):
    soma = 0
    for i in range (0, len(vector)-1):
        soma += matriz_distance[vector[i]][vector[i+1]]
    return soma + matriz_distance[vector[0]][vector[-1]]

def acumular(v):
    res = []
    acum = 0
    for i in v:
        res.append(i + acum)
        acum = res[-1]
    return res

def random_select(pop, f, matriz):
    fit = []
    for p in pop:
        fit.append(1/f(p, matriz))
    soma = sum(fit)
    norm = map(lambda x: x/soma, fit)

    acm = acumular(norm)
    r = random.random()  # retorna um numero entre 0 e 1

    for i in range(len(acm)):
        if r < acm[i]:  # verifica em qual intervalo o numero aleatorio esta
            return pop[i]



def genetico(pop_inicial, f, estagnacao, tx_mutacao, matriz, use_crossover_alternativo=False, id_mutacao=1, elitismo=False):


    return pop_inicial
