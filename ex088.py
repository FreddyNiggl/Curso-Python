"""Crie um progrma que ajude a criar palpites de megasena de 6 numeros dentro de uma
 unica lista."""

import random
print('-=' * 20)
mega = 'MEGA SENA'
print(f'{mega:^40}')
print('-=' * 20)

print('Quantos jogos voce deseja ? ')
qt = int(input('-> '))
print('_-' * 20)
jogos = []
for j in range(0, qt, 1):
    for i in range(0, 6):
        jogos.append(random.randint(1, 60))
    print(jogos)
    print('_-'* 20)
    jogos = []


