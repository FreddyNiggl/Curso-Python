# crie um programa que leia varios numeros inteiros e so pare
# ao receber 999 mostre quanto sumeros foram digitados desconsiderando o flag.
contador = 0
num = ''
while num != 999:
    num = int(input('Digite seus numeros ai humano...  '))
    contador = contador + 1
    if num == 999:
        contador = contador - 1

print('Foram digitados {} numeros'.format(contador))


