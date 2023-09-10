import math as m

print('-=-' * 20)
print('<Programa de coordenadas transladas>')
print('-=-' * 20)

x = int(input('Digite o ponto X de origem translada: '))
y = int(input('Digite o ponto Y de origem translada: '))
n = int(input('Digite o número de pontos a ser utilizados: '))
quad = ""
dist = 0
aux = 0

for i in range(1, n+1):
    p_x = int(input('Digite a posição x do ponto: '))
    p_y = int(input('Digite a posição y do ponto: '))
    if p_x == x or p_y == y:
        print('Ponto ({}, {}) esta no eixo coordenado.'.format(p_x, p_y) )
    else:
        if p_x > x and p_y > y:
            quad = 1
        elif p_x < x and p_y > y:
            quad = 2
        elif p_x < x and p_y < y:
            quad = 3
        elif p_x > x and p_y < y:
            quad = 4
        print('Ponto ({}, {}) esta no {}° quadrante'.format(p_x, p_y, quad))
    aux =  dist
    dist = m.sqrt(m.pow(x - p_x, 2) + m.pow(x - p_x, 2))
    if aux <= dist:
        maior = dist 
    elif dist <= aux:
        menor = dist
    print('Ponto ({}) eh o mais proximo, distancia= {}')