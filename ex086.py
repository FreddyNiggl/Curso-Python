""" Crie um programa que crie uma matriz 3x3 e receba valores do ussuario e no final mostre
a posicao de cada valor correspondete com sua posicao"""

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
print(lista_conjunta)

linha_lista_conjunta_1 = lista_conjunta[0:3]
linha_lista_conjunta_2 = lista_conjunta[3:6]
linha_lista_conjunta_3 = lista_conjunta[6:9]

print(linha_lista_conjunta_1)
print(linha_lista_conjunta_2)
print(linha_lista_conjunta_3)








# contador = 0
# while contador < len(lista_conjunta)-1:
#     if contador == 3:
#         print()
#     print(lista_conjunta[0][contador])
#     contador += 1
