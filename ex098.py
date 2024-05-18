"""Crie uma funcao chamada CONTADOR que receba a entrada de 3 valores INICIO FIM e PASSO e no final
deve mostrar a contagem de 1 -10 em 1-1
de 10 - 0  em 2-2
e uma contagem personalizada."""

from time import sleep


def cai10_1():
    for i in range(10, 0, -1):
        print(f'{i}', end=' ')
        sleep(0.5)
    print('FIM')
    print('~' * 15)


def sobe1_10():
    for i in range(1, 11, 1):
        print(f'{i}', end=' ')
        sleep(0.5)
    print('FIM')
    print('~' * 15)


cai10_1()
sobe1_10()


def personal(a, b, c):
    if c == 0:
        c = 1
    if a > b:
        c = - abs(c)
        b = b - 1
    elif b > a:
        c = abs(c)
        b = b + 1
    for i in range(a, b, c):
        print(f'{i}', end=' ')
        sleep(0.5)


print('Sua vez: ')
personal(
    a=int(input('Digite o valor de inicio: ')),
    b=int(input('Digite o valor do final: ')),
    c=int(input('Digite o valor do passo a passo: ')))



