'''Cria um programa que gera 5 numeros aleatorios e os coloca em uma tuploa
em seguida mostre a listagem dos numeros gerados e qual o menor e o maior '''
import random
tuplas = ()
for i in range(0, 5):
    num = random.randint(0, 10)
    tupla = (num,)
    tuplas = tuplas + tupla
    if i == 0:
        maior_numero = tuplas[i]
        menor_numero = tuplas[i]
    else:
        if tuplas[i] > maior_numero:
            maior_numero = tuplas[i]
        elif tuplas[i] < menor_numero:
            menor_numero = tuplas[i]
print(tuplas)
print(f'Maior = {maior_numero}')
print(f'Menor = {menor_numero}')