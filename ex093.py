"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feito em cada partida.
No final, tudo isso sera guardado em um dicionario, incluindo o total de gols feitos durante o campeonato"""

pont_jogos = []
play_rendiment = {}
pont_total = 0

play_rendiment['jogador'] = str(input('Qual o nome do jogador? '))
play_rendiment['partidas'] = int(input('Qunatas partidas ele jogou? '))
print('Qual a pontuacao em cada jogo? ')
for i in range(0, play_rendiment['partidas']):
    gols = int(input(f'Gols no {i+1}° jogo: \n-> '))
    pont_jogos.append(gols)
for i in pont_jogos:
    pont_total += i
print(pont_total)
play_rendiment['ponto_partidas'] = pont_jogos
play_rendiment['ponto_total'] = pont_total

print(play_rendiment)
print('-=' * 30)
print(f'O jogador {play_rendiment['jogador']} jogou {play_rendiment['partidas']} partidas.')

seta = '=>'
for i in range(0, len(play_rendiment['ponto_partidas'])):
    print(f'{seta:>10} Na partida {i+1}°, fez {play_rendiment['ponto_partidas'][i]} gols. ')
print(f'Foi um total de {play_rendiment['ponto_total']} gols.')