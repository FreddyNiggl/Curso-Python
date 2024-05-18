# leia varios numeros ate ser digitado 999;
# no final mostre a soma totoal dos numeros e quantos foram digitados


print('*' * 21)
print(' REGISTRANDO NUMEROS')
print('*' * 21)
num = 0
contador = 0
soma = 0
while num != 999:
    print('Digite seu numero: ')
    num = int(input('->  '))
    if num == 999:
        break
    else:
        soma = soma + num
        contador = contador + 1

print(f'A soma dos {contador} numeros é = {soma}')

