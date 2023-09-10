from math import pow

print('-=-'*20)
print('Programa que descobre se um triangulo e retangulo: ')

l1 = int(input('Digite o lado 1: '))
l2 = int(input('Digite o lado 2: '))
l3 = int(input('Digite o lado 3: '))
if l1 >= l2 and l1 >= l3:
    hip = l1
    cat1 = l2
    cat2 = l3

if l2 >= l1 and l2 >= l3:
    hip = l2
    cat1 = l1
    cat2 = l3

if l3 >= l1 and l3 >= l2:
    hip = l3
    cat1 = l1
    cat2 = l2

print('Hpotenusa = {}, cateto 1 e 2 = {}, {}'.format(hip, cat1, cat2))

if pow(hip, 2) == (pow(cat1, 2) + pow(cat2, 2)):
    print('Os lados formam triangulo')
else: 
    print('Os lados não formam triangulo')

print('FIM')
print('-=-'*20)
    
    

