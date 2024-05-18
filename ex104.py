"""Crie um programa que tenha a funcao LEIAINT() que vai funcionar de forma semelhante a funcao INPUT() do
PYTHON. So que fazendo a validacao para aceitar apenas um valor numerico"""


def leiaint(valor):
    # ok = False
    while True:
        n = str(input(valor))
        if n.isnumeric():
            valor = int(n)
            return valor
            # ok = True
        else:
            print('\033[0;31m ERRO!Tente novamente. \033[m')
        # if ok:
            # break
    # return valor


n = leiaint('Digite valor numerico: ')
print(f'Voce acabou de digitar o numero {n}')
