"""Escreva uma tulpa de numeros por extensao de 0 - 20.
seu programa devera ler um numero pelo teclado e mostrálo por extenso """

tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:

    print('Digite um numero de 0 - 20')
    num = int(input('->  '))
    while 0 > num or num > 20:
        print('Valor inválido, tente novamente um valor')
        num = int(input('->  '))

    extenso = tupla[num]
    print(extenso)

    print('Deseja continuar? [ S / N ]')
    continuar = str(input('->  ')).upper().strip()[0]
    while continuar not in 'SN':
        print('Entrada invalida, tente novamente.')
        continuar = str(input('->  ')).upper().strip()[0]
    if continuar == 'N':
        break
