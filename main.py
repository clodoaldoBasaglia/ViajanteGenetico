#!/usr/bin/python
#coding: utf-8

import math, random, copy,sys
from matplotlib import pyplot as plt


def formatar_coord(file):
    header = {}
    for i in range(5):
        content = file.readline().strip('\n').replace(' : ', ': ').split(': ')
        # print content
        header[content[0]] = content[1]
    file.readline()
    coordenadas = [0 for i in range(0, int(header['DIMENSION']) + 1)]

    for i in range(int(header['DIMENSION'])):
        line = file.readline()
        line = line.strip('\n').lstrip()
        content = line.split(' ')
        content = filter(None, content)
        print(content)
        # print content
        #id = content[0]
        coordenadas[int(content[0])] = int(content[1]) + ' ' + int(content[2])

    return coordenadas, header


def gerar_matriz(header, coordenadas):
    matriz = [[0 for i in range(0, int(header['DIMENSION']) + 1)]
              for i in range(0, int(header['DIMENSION']) + 1)]
    for origem in range(1, int(header['DIMENSION']) + 1):
        for destino in range(1, int(header['DIMENSION']) + 1):
            if origem != destino:
                origem_cordenates = coordenadas[origem].split(' ')
                destino_cordenates = coordenadas[destino].split(' ')
                x = [float(origem_cordenates[0]), float(destino_cordenates[0])]
                y = [float(origem_cordenates[1]), float(destino_cordenates[1])]
                matriz[origem][destino] = distancia_euclidiana(x, y)
    return matriz

def main(argv):
    file = open(argv[1], 'r')

    coordenadas, header = formatar_coord(file)


    matriz = gerar_matriz(header, coordenadas)


    pop = genetico.gerar_populacao(200, int(header['DIMENSION']))

    resultados = genetico.genetico(
        pop, genetico.fitness, 15, 5, matriz, elitismo=False, use_crossover_alternativo=True, id_mutacao=2)
    print(header['NAME'])
    for resultado in resultados:
        print(resultado)


if __name__ == "__main__":
    main(sys.argv)