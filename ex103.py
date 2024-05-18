"""Faca um programa ue tenha uma funcao chamada FICHA() que receba dois valores opcionais:
o NOME de um jogador e QUANTOS GOLS ele marcou.
O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado
corretamente"""


def jogador(name='<Indefinido>', gols=0):
    print(f'O {name} fez {gols} gols na partida')


nome = str(input('NOME:\n-> '))
gol = str(input('GOLS:\n-> '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if nome.strip() == '':
    jogador(gols=gol)
else:
    jogador(nome, gol)
