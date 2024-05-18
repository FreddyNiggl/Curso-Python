"""Crie uma funcao FATORIAL() que receba 2 parametros o primeirou que indica o numero a ser calculado
e o outro  sera  um chamado SHOW, que sera um valor logico(opcional) indicando se sera mostrado ou nao na tela
o processo de calculo do fatorial"""


def fatorial(num=0, show=False):
    if show:
        fat = 1
        print(f'Fatorial de !{num} :', end='')
        for i in range(1, num + 1, 1):
            fat *= i
            if i == num:
                print(f' {i}')
            else:
                print(f' {i} x', end='')
    else:
        fat = 1
        for i in range(1, num + 1, 1):
            fat *= i
        print(f'Fatorial de !{num} é {fat}')


num = int(input('Digite um numero para ver seu fatorial: \n-> '))
show = str(input('Deseja ver a operacao fatorial ? [True/ False]\n -> ').upper().strip()[0])
while show not in 'TF':
    print('Valor nao reconhecido. Tente novamente')
    show = str(input('Deseja ver a operacao fatorial ? [True/ False]\n -> ').upper().strip()[0])
if show == 'T':
    show = True
elif show == 'F':
    show = False

fatorial(num, show)
