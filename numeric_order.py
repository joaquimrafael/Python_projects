print('-=-'*30)
print('Programa de ordenamento crescente de numeros')

n1 = int(input('Digite o n1: '))
n2 = int(input('Digite o n2: '))
n3 = int(input('Digite o n3: '))

if n1 > n2 and n1 > n3 and n2 > n3:
    print('A ordem e', n3, n2, n1)
    
if n1 > n3 and n1 > n2 and n3 > n2:
    print('A ordem e', n2, n3, n1)

if n2 > n1 and n2 > n3 and n1 > n3:
    print('A ordem e', n3, n1, n2)

if n2 > n1 and n2 > n3 and n3 > n1:
    print('A ordem e', n1, n3, n2)

if n3 > n1 and n3 > n1 and n1 > n2:
    print('A ordem e', n2, n1, n3)

if n3 > n1 and n3 > n2 and n2 > n1:
    print('A ordem e', n1, n2, n3)

if n1 == n2 and n1 > n3 and n2 > n3:
    print('A ordem e', n3, n2, n1)

if n1 == n3 and n1 > n2 and n3 > n2:
    print('A ordem e', n2, n3, n1)

if n2 == n3 and n2 > n1 and n3 > n1:
    print('A ordem e', n1, n3, n2)

if n1 == n2 and n1 < n3 and n2 < n3:
    print('A ordem e', n2, n1, n3)
    
if n1 == n3 and n1 < n2 and n3 < n2:
    print('A ordem e', n3, n1, n2)

if n2 == n3 and n2 < n1 and n3 < n1:
    print('A ordem e', n3, n2, n1)
    
if n1 == n2 and n1 == n3:
    print('A ordem e', n1, n2, n3)
    
print('FIM')
print('-=-'*30)
