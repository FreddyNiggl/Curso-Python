'''Crie uma tupla com os 20 times do brasileirao e mostre
os 5 primeiros colcados
os ultimos 4 colocados
a tupla em ordem alfabetica
a posicao do time da chapecoense
'''

tupla = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo',
          'Vasco', 'Chapecoense', 'Atletico', 'Botafogo', 'Atletico_PR',
          'Bahia', 'Sao paulo', 'Fluminense', 'Sporte recife', 'EC vitoria',
          'Coritiba', 'Avai', 'Pontepreta', 'Atletico-GO')

print('-' * 100)
print(f'Os 5 primeiros colocados sao {tupla[0:5]}')
print('-' * 100)
print(f'Os ultimos 4 colocados foram {tupla[-1:-5:-1]}')
print('-' * 100)
print(f'Em ordem alfabética fica: {sorted(tupla)}')
print('-' * 100)
print(f'A posicao do time da Chapeconense é: {tupla.index('Chapecoense') + 1}° lugar')
print('-' * 100)


