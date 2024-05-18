# faca a leitura de 6 numeros inteiros e some apenas entre eles os pares.

soma = 0
for i in range(1, 6 + 1):
    numero = int(input('Digite um numero inteiro: '))
    if numero % 2 == 0:
        soma = soma + numero
        print('{} é par'.format(numero))

print('A soma deles eh: {}'.format(soma))
