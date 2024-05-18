# ler um numero inteiro e dizer se é um numero primo
numero = int(input('Digite um numero: '))

contador = 0
for i in range(1, numero+1, 1):
    if numero % i == 0:
        contador = contador + 1
print(contador)
if contador == 2:
    print('O numero {} é um numero primo!'.format(numero))
else:
    print('O numero {} não é primo!'.format(numero))

