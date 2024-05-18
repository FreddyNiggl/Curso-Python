# faca um programa que mostre a tabuada de varios numeros uma por vez e so pare quando
# inserido um valor negativo

print('*' * 10)
print(' TABUADAS')
print('*' * 10)
num = 0
print('Digite o numero o qual deseja ver a tabuada(valos negativo para sair)')
num = int(input('->  '))
while num >= 0:
    print('#' * 20)
    for n in range(1, 11, 1):
        multi = num * n
        print(f'{num} * {n} = {multi}')
    print('#' * 20)
    print('Digite o numero o qual deseja ver a tabuada(valos negativo para sair)')
    num = int(input('->  '))

print('FIM...')
