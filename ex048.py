# calcule a soma de todos numeros impares multiplos de 3  de 1 - 500
soma = 0
for i in range(1, 500+1, 2):
    if i % 3 == 0:
        soma = soma + i
        print('{} é um numero impar e multiplo de 3'.format(i))
print('A soma de todos esse é = {} '.format(soma))
print('Fim...')