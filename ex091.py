"""crie um programa onde 4 jogadores jogam um dado e tenham resutados aleatoorios.
guarde essas resultados em um dicionario.
coloque esse dicionario em ordem
sabendo que o vencedor tiroi o maior numero do dado"""
# import random
#
# dici_valores = {}
# lista_ordem = []
# maior = 0
#
# for i in range(0, int(input('Quantas pessoas vao jogar ? ')), 1):
#     val_dado = random.randint(1, 6)
#     if i == 0:
#         maior = val_dado
#     elif val_dado > maior:
#         maior = val_dado
#     lista_ordem.append(val_dado)
#     lista_ordem.sort()
#
# for i, v in enumerate(lista_ordem):
#     dici_valores['jogada_' + f'{i}'] = v
#     print(f'A {i+1}° jogada teve valor = {dici_valores['jogada_' + f'{i}']} \n')

######################################################################################3

import random
import time
import operator
jogo = {
    'jogador1': random.randint(1, 6),
    'jogador2': random.randint(1, 6),
    'jogador3': random.randint(1, 6),
    'jogador4': random.randint(1, 6)}
ranking = list()
print('valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    time.sleep(1)
ranking = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i,v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')