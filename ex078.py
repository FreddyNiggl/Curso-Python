"""ler 5 valores numericos e guardar em uma lista
mostre qual o maior e o menor e suas posicoes"""

lista = []
for i in range(0, 5):
    print('Digite um numero: ')
    lista += [int(input('-> '))]
    if i == 0:
        maior_numero = lista[0]
        menor_numero = lista[0]
    elif lista[i] > maior_numero:
        maior_numero = lista[i]
    elif lista[i] < menor_numero:
        menor_numero = lista[i]

print(f'Os valores digitados foram {lista}')
print(f'O maior numero digitado foi: {maior_numero} nas posicoes: ', end='')
for ind, val in enumerate(lista):
    if val == maior_numero:
        print(f'{ind}...', end='')
print(f'\nO menor numero digitado foi: {menor_numero} nas posicoes: ', end='')
for ind, val in enumerate(lista):
    if val == menor_numero:
        print(f'{ind}...', end='')