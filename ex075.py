"""Crie um programa que leia 4 valores pelo teclado e guarde-os em uma tupla
depois diga:
quantas vezes apareceu o numero 9
em que posicao foi digitado o primeiro numero 3
quais foram os numeros pares"""

tuplas = ()
tupla_par = ()
cont_par = 0
vez9 = 0
for i in range(1, 5, 1):
    print('Digite um valor: ')
    valor = int(input('->  '))
    tupla = (valor,)
    tuplas = tuplas + tupla
    if valor == 9:
        vez9 += 1
    if valor == 3:
        vez3 = tuplas.index(3) + 1
    if valor % 2 == 0:
        cont_par += 1
        tupla_par += (valor,)

if vez3 is not None:
    print(f'O numero 3 aparece na posicao: {vez3}°')
else:
    print(f'O numero 3 nao aparece nenhuma vez.')

print(f'O numero 9 aparece : {vez9} vezes')
print(f'O total de numeros pares foi: {cont_par}')
print(f'Os numeros pares foram: {tupla_par}')
