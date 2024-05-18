"""Crie uma funcao que receba varios numeros e depois mostre qual deles é o maior   """


# def numeros():
#     lista = []
#     while True:
#         lista.append(int(input('Insire um valor numerico: \n-> ')))
#         cont = str(input('Deseja continuar ? [S / N]\n-> ')).upper().strip()[0]
#         while cont not in 'SN':
#             print('Valor invalido. Tente novamente.')
#             cont = str(input('Deseja continuar ? [S / N]\n-> ')).upper().strip()[0]
#         if cont == 'N':
#             break
#     print(f'O maior valor é {max(lista)}')
#
# numeros()

#############################################################################################

def numeros(*num):
    print(f'O maior valor é {max(lista)}')


lista = []
while True:
    lista.append(int(input('Insire um valor numerico: \n-> ')))
    cont = str(input('Deseja continuar ? [S / N]\n-> ')).upper().strip()[0]
    while cont not in 'SN':
        print('Valor invalido. Tente novamente.')
        cont = str(input('Deseja continuar ? [S / N]\n-> ')).upper().strip()[0]
    if cont == 'N':
        break

numeros(lista)

