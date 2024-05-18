# melhore o jogo do ex 28 com while e diga quantas tentativas foram usadas
import random
import time

resp = 0
while resp != 2:
    print('Tente adivinhar em que numero estou pensando...')
    resp = str(input('[ 1 ] - SIM\n'
                     '[ 2 ] - NAO\n'
                     'Aceita o desafio ?  '))
    pc = random.randint(1, 10)
    print('Vamos lá, Eu sou otimo nesse jogo hehe...')
    print('Faca sua escolha: ')
    print('Em que numero pensei? hehe...')
    user = int(input('Sua Escolha(1 - 10):  '))

    time.sleep(1)
    print('Vamos la...')
    time.sleep(1)

    if pc == user:
        print('UAU voce VENCEU! "Nao deve ser humano, isso é trapaça!"')
    else:
        print('Como o esperado, nenhum humano pode me vencer haha...\n'
              'Tente contra uma galinha da proxima vez.')

    time.sleep(2)
    print('Deseja tentar novamente ^_^ ? ')
    print('-=' * 20)
    print('[ 1 ] - SIM\n''[ 2 ] - NAO')
    print('-=' * 20)
    resp = int(input('Sua resposta:  '))
