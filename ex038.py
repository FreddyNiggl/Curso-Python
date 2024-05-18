# compare dois numeros e diga qual é o maior ou se sao iguais

print('Hora de comparar')
n1 = int(input('Digite o 1° numero: '))
n2 = int(input('Digite o 2° numero: '))

if n1 > n2:
    print('{} eh maior que {}'.format(n1,n2))
elif n2 > n1:
    print('{} eh maior que {}'.format(n2, n1))
else:
    print('{} é igual a {}'.format(n1, n2))
