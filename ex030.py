# Ler um numero inteiro dito pelo usuario e
# dizer se ele é par ou impar

n = int(input('Digite um numero:'))

if n % 2 == 0:
    print('O numero {} é par'.format(n))
else:
    print('O numero {} é impar'.format(n))