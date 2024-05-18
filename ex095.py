"""aprimore o ex 93 para que ele funcione para varios jogadores, incluindo um sistema
de visualizaçao de detalhes do aproveitamnto de cada jogador"""
pont_jogos = []
play_rendiment = {}
pont_total = 0
dici_jogadores = {}

qt_jogadores = int(input('Quantos jogadores voce quer registrar ?\n -> '))
for j in range(0, qt_jogadores, 1):
    play_rendiment['jogador'] = str(input('Qual o nome do jogador? '))
    play_rendiment['partidas'] = int(input('Qunatas partidas ele jogou? '))
    print('Qual a pontuacao em cada jogo? ')
    for i in range(0, play_rendiment['partidas']):
        gols = int(input(f'Gols no {i + 1}° jogo: \n-> '))
        pont_jogos.append(gols)
    for i in pont_jogos:
        pont_total += i
    play_rendiment['ponto_partidas'] = pont_jogos.copy()
    play_rendiment['ponto_total'] = pont_total
    print(play_rendiment)

    dici_jogadores['jog_' + f'{j}'] = play_rendiment.copy()

    pont_jogos.clear()
    play_rendiment.clear()
    pont_total = 0
print(dici_jogadores)
print(play_rendiment)

print('-=' * 40)
print(f'{"cod":<5} {"nome":<8} {"total":<6} {"gols":<12}')
for i in range(0, qt_jogadores, 1):
    print(f'{i:<5} {dici_jogadores["jog_" + f"{i}"]["jogador"]:<9}'
          f'{dici_jogadores["jog_" + f"{i}"]["ponto_total"]:<7}'
          f'{dici_jogadores["jog_" + f"{i}"]["ponto_partidas"]}')
mostrar = int(input('Mostrar os dados de qual jogador? [N° cod] [999 - encerra]'))
while mostrar != 999:
    if mostrar > qt_jogadores - 1:
        print('Valor invalido. Tente novamente.')
    elif mostrar < 0:
        print('Valor invalido. Tente novamente.')
    elif mostrar <= qt_jogadores:
        for i in range(0, len(dici_jogadores["jog_" + f"{mostrar}"]["ponto_partidas"]), 1):
            print(f'No jogo {i + 1} fez {dici_jogadores["jog_" + f"{mostrar}"]["ponto_partidas"][i]}')
    if mostrar == 999:
        print('Ate logo! FIM...')
        break
    mostrar = int(input('Mostrar os dados de qual jogador? [N° cod] [999 - encerra]'))
