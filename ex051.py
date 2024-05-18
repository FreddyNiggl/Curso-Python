# leia o primeiro termo  e a razao de uma PA. no final,
# mostre os 10 primeiros termos  desa progressao

num1 = int(input('Digite o primeiro numero da PA'))
razao = int(input('Digite o valor da Razao'))

indice = 1
for i in range(num1, num1*10, razao):
    print('O {}° termo dessa PA e: {}'.format(indice, i))
    indice = indice + 1

print('Fim...')