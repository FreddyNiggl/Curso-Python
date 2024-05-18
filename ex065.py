# crie um programa que leia n numeros inteiros no final mostre a media entre
# os valores digitados, qual o maior e qual o menor. O programa deve perguntar
# se ele deseja continuar a digitar valores.

print('Digite quantos numeros precisar')
soma = 0
contador = 0
maior_num = 0
menor_num = 0
continuar = 1
while continuar != 2:
    num = int(input('Digite um numero: '))
    contador = contador + 1
    soma = soma + num
    media = soma / contador

    if contador == 1:
        maior_num = num
        menor_num = num
    else:
        if num > maior_num:
            maior_num = num
        elif num < menor_num:
            menor_num = num

    print('Deseja continuar ?')
    continuar = int(input('[ 1 ] - SIM\n'
                          '[ 2 ] - NAO\n'
                          'Sua escolha: '))

print('A media dos numeros digitados e: {}'.format(media))
print('O maior numero digitado e: {}'.format(maior_num))
print('O menor numero digitado e: {}'.format(menor_num))
