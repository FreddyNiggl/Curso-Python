"""Faca um programa que leia o nome e o peso de varias pessoas e os guarde em umas lista
Qunatas pessoas foram cadastradas
uma lista com as pessoas mais pesadas
uma lista com as pessoas mais leves"""
tabela_cadastro = list()
nome_peso = []
contador = 0
mais_peso = 0
menos_peso = 0
nome_pesados = []
nome_leve = []
while True:
    print('Cadastre o nome: ')
    nome = str(input('-> '))
    nome_peso.append(nome)

    print('Cadastre peso: ')
    peso = int(input('-> '))
    nome_peso.append(peso)

    tabela_cadastro.append(nome_peso[:])
    contador += 1

    print(tabela_cadastro)
    print(nome_peso)

    if len(tabela_cadastro) == 1:
        mais_peso = nome_peso[1]
        menos_peso = nome_peso[1]
    else:
        contador = 0
        while contador < len(tabela_cadastro):
            if tabela_cadastro[contador][1] > mais_peso:
                mais_peso = tabela_cadastro[contador][1]
            elif tabela_cadastro[contador][1] < menos_peso:
                menos_peso = tabela_cadastro[contador][1]
            contador += 1

    if len(nome_peso) >= 0:
        del nome_peso[1]
        del nome_peso[0]

    continuar = str(input('Deseja continuar ? [Sim/ Nao]')).strip()[0]
    while continuar not in 'SsNn':
        print('Entrada invalida. Tente novamente')
        continuar = str(input('Deseja continuar ? [Sim/ Nao]')).strip()[0]
    if continuar in 'Nn':
        break

for i in range(0, len(tabela_cadastro)):
    if tabela_cadastro[i][1] == mais_peso:
        if tabela_cadastro[i][0] not in nome_pesados:
            nome_pesados.append(tabela_cadastro[i][0])
    elif tabela_cadastro[i][1] == menos_peso:
        if tabela_cadastro[i][0] not in nome_leve:
            nome_leve.append(tabela_cadastro[i][0])

print(f'Tivemos um total de {contador} pessoas cadastradas.')
print(f'{tabela_cadastro}')
print(f'{nome_pesados} sao os mais pesados')
print(f'{nome_leve} sao os menos pesados')
# print(mais_peso)
# print(menos_peso)
