"""Crie uma funcao que receba um texto e print ele com linhas()margem em cima e embaxio adaptativas.
elas devem acompanhar o tamanho do texto passado"""


def texto(txt):
    s = (len(txt) + 4)
    print('~' * s)
    print(f'{'  '}{txt} {'  '}')
    print('~' * s)


texto('Hoje está um lindo dia')

texto('Bom dia amor')

texto('Que dia bom para feedar heheheh')