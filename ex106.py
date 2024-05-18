"""Faca um mini-sistema que o utilize o interative HELP do pytohn.
O ususario vai digitar o comando e o manual vai aparecer.
Quando o ususario digitar a palavra 'fim' o programa se encerrara
OBS: USe cores"""


def textualizado1():
    print('\033[0;30;42m~' * (len('SISTEMA DE AJUDA PyHELP') + 4))
    print(f'\033[0;30;42m  {'SISTEMA DE AJUDA PyHELP'}')
    print('~' * (len('SISTEMA DE AJUDA PyHELP') + 4))

def textualizado2(comando):
    print('\033[m''\033[0;30;44m~' * (len(f'Acessando o Manual do comando {comando}') + 4))
    print(f'{f'Acessando o Manual do comando {comando}'}')
    print('~' * (len(f'Acessando o Manual do comando {comando}') + 4))


def textualizado3(descricao):
    while descricao != 'fim':
        textualizado1()
        textualizado2(f'"{descricao}"')
        print('\033[m' '\033[7;38;40m')
        print(help(descricao))
        textualizado3((input('\033[m''Funcao ou Biblioteca > ')))


textualizado3(str(input('Funcao ou Biblioteca > ')))
