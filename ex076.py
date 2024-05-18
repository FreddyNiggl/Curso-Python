"""crie um progrma que tenha uma tupla unica com seus respectivos valores na sequencia
no final mostre a listagem de precos organizando os dados de forma tabular"""

print('_' * 50)
titulo = 'LISTAGEM DE PREÇOS'
print(f'{titulo:^50}')
print('_' * 50)

tuplas = ()
while True:
    print('Digite o nome do produto desejado: ')
    nome = str(input('-> ')).title().strip()
    print('O valor do produto: ')
    val = float(input('-> R$ '))
    tupla = (nome, val)
    tuplas += tupla

    print('Deseja continaur ? [Sim / Nao]')
    continuar = str(input('-> ')).upper().strip()[0]
    while continuar not in 'SN':
        print('Deseja continaur ? [Sim / Nao]')
        continuar = str(input('-> ')).upper().strip()[0]
    if continuar == 'N':
        break


print('-' * 50)
titulo = 'LISTAGEM DE PREÇOS'
print(f'{titulo:^50}')
print('-' * 50)
for i in range(0, len(tuplas), 2):
    print(f'{tuplas[i]:.<40}R$ {tuplas[i+1]:>6}')

print('_'* 50)