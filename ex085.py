"""Crie um programa onde o ussuario digita 7 valores numericos e cadastre em uma lista unica que
mantenha separados os numeros pares dos impares no final, mostre os valores pares dos impares em ordem crescente"""
lista_conjunta = []
lista_pares = []
lista_impares = []

for i in range(0, 7, 1):
    print('Digite um valor numerico: ')
    valor = int(input('-> '))
    if valor % 2 == 0:
        lista_pares.append(valor)
        lista_pares.sort(reverse=True)
    else:
        lista_impares.append(valor)
        lista_impares.sort()

lista_conjunta.append(lista_pares)
lista_conjunta.append(lista_impares)

print(f'A lista final é {lista_conjunta}')
