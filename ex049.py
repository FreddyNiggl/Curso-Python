# faca uma tabuada utilizando de for
numero = int(input('Digite um numero para efetuar a tabuada:'))

for i in range(0, 10+1):
    valor = numero * i
    print('{} x {} = {}'.format(numero, i, valor))

print('Fim...')