# Ler tres numeros e dizer qual o maior e qual o menor

print('Digite 3 numeros: ')
n1 = int(input('Digite o 1° numero:'))
n2 = int(input('Digite o 2° numero:'))
n3 = int(input('Digite o 3° numero:'))

n1_maior = n1 > n2
n2_maior = n2 > n3
n3_maior = n1 > n3

if n1_maior == True and n2_maior == True:
    print('{} é o maior e o {} o menor'.format(n1, n3))

elif n2_maior == True and n3_maior == False:
    print('{} é o maior e o {} o menor'.format(n2, n1))

elif n2_maior == False and n3_maior == True:
    print('{} é o maior e o {} o menor'.format(n1, n2))

elif n1_maior == False and n2_maior == True and n3_maior == True:
    print('{} é o maior e o {} o menor'.format(n2, n3))

elif n1_maior == False and n3_maior == False and n2_maior == False:
    print('{} é o maior e o {} o menor'.format(n3, n1))

elif n2_maior == False and n1_maior == False:
    print('{} é o maior e o {} o menor'.format(n3, n1))

elif n3_maior == False and n2_maior == False and n1_maior == True:
    print('{} é o maior e o {} o menor'.format(n3, n2))

elif n3_maior == False and n2_maior == False and n1_maior == False:
    print('{} é o maior e o {} o menor'.format(n3, n1))
