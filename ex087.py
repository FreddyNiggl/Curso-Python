"""Continue o exercicio 86 mostrando  a soma_tot de todos os valores pares, a soma_tot dos valores da terceira
coluna e o maior valor da 2 linha"""

lista_conjunta = []
for i in range(0, 3, 1):
    for j in range(0, 3, 1):
        print(f'Digite o valor para a posicao {i}, {j}: ')
        valor = [int(input('-> '))]
        lista_conjunta.append(valor)

print('-=' * 20)
text = 'MATRIZ 3X3'
print(f'{text:^40}')
print('-=' * 20)

linha_lista_conjunta_1 = lista_conjunta[0:3]
linha_lista_conjunta_2 = lista_conjunta[3:6]
linha_lista_conjunta_3 = lista_conjunta[6:9]

print(linha_lista_conjunta_1)
print(linha_lista_conjunta_2)
print(linha_lista_conjunta_3)

print('-=' * 20)

soma_tot = 0
for i, v in enumerate(lista_conjunta):
    if v[0] % 2 == 0:
        soma_tot += v[0]

soma_3c = 0
for i in range(2, len(lista_conjunta), 3):
    soma_3c += lista_conjunta[i][0]

maior = 0
for i in range (len(linha_lista_conjunta_2)):
    if i == 0:
        maior = linha_lista_conjunta_2[i][0]
    elif linha_lista_conjunta_2[i][0] > maior:
        maior = linha_lista_conjunta_2[i][0]

print(f'A soma total dos valores pares eh: {soma_tot}')
print(f'A soma da 3 coluna dos valores eh: {soma_3c}')
print(f'O maior numero na 2° linha eh: {maior}')
