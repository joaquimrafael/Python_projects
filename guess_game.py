from random import randint
from time import sleep
comp = randint(0, 5)  # faz o computador pensar
print('\33[33m-=-\33[m'*20)
print('\33[1;31mVou pensar em um número entre 0 e 5. Tente adivinhar...\33[m')
print('\33[33m-=-\33[m'*20)
jog = int(input('Em que número pensei? '))  # Jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)
if comp == jog:
    print('Meus parabéns! Você advinhou!!')
else:
    print('Não foi dessa vez, eu pensei no número {} e não no {}'.format(comp, jog))
print('\33[4;30;107mEND\33[m')
print('¨'*65)


