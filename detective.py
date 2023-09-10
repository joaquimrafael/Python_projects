print('Programa detetive...')
perg1 = input('Telefonou para a vítima? ').lower()
perg2 = input('Esteve no local do crime? ').lower()
perg3 = input('Mora perto da vítima? ').lower()
perg4 = input('Devia para a vítima? ').lower()
perg5 = input('Já trabalhou com a vítima? ').lower()
soma = 0
if perg1 == 'sim':
    soma += 1
if perg2 == 'sim':
    soma += 1
if perg3 == 'sim':
    soma += 1
if perg4 == 'sim':
    soma += 1
if perg5 == 'sim':
    soma += 1
if soma == 2:
    print('Suspeita')
elif (soma >= 3) and (soma <= 4):
    print('Cúmplice')
elif soma == 5:
    print('Assasino')
else:
    print('Inocente')


