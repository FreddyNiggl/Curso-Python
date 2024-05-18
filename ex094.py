"""Crie um program que leia o NOME, SEXO,  e IDADE de varias pessoas guardando
os dados de cada pessoa em um dicioanrio e todos os dicionarios em uma lista.
 NO final mostre:
 -quantas pessoas foram cadastradas:
 -a media de idade do grupo
 -uma lista com todas as mulheres
 -Uma lista com todas as pessoas  com idade acima da media"""

lista_cadastro = []
cadastro = {}
contador = 0
tot = 0

while True:
    cadastro['nome'] = str(input('Qual seu nome? \n-> '))
    cadastro['sexo'] = str(input('Qual seu sexo? \n-> '))
    cadastro['idade'] = int(input('Qual sua idade? \n-> '))

    contador += 1

    lista_cadastro.append(cadastro.copy())
    cadastro.clear()

    continuar = str(input('Deseja continuar cadastrando ? \n-> ')).strip()[0]
    while continuar not in 'SsNn':
        print('Valor invalido. Tente novamente.')
        continuar = str(input('Deseja continuar cadastrando ? \n-> ')).strip()[0]
    if continuar in 'Nn':
        break

mulher = []
acima_idade = []
for i in range(0, contador, 1):
    tot += lista_cadastro[i][f'{'idade'}']
    media = tot / contador
    if lista_cadastro[i][f'{'sexo'}'] in 'Mm':
        mulher.append(lista_cadastro[i][f'{'nome'}'])

for i in range(0, contador, 1):
    if lista_cadastro[i][f'{'idade'}'] > media:
        acima_idade.append((lista_cadastro[i][f'{'nome'}']))

print(f'Foram cadastradas {contador} pessoas.')
print(f'A idade media foi de {media:.2f} anos')
print(f'As mulheres foram {mulher}')
print(f'As pessoas acima da media de idade do grupo sao {acima_idade}')

print('FIM...')
