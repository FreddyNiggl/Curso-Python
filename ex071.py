# Fazer um caixa eletronico e dizer quantas notas de cada cedula o cleinte ira receber
# com seu valor de saque. o caixa tem notas de 50, 20, 10, 1

print('*' * 20)
print('CAIXA ELETRONICO')
print('*' * 20)

sair = False
while not sair:
    prosseguir = False

    print('Quanto voce deseja sacar ? ')
    sacar = int(input('-> '))

    notas_50 = sacar // 50
    sacar = sacar % 50
    notas_20 = sacar // 20
    sacar = sacar % 20
    notas_10 = sacar // 10
    sacar = sacar % 10
    notas_1 = sacar // 1

    print('Serao necessarias:')
    if notas_50 > 0:
        print(f'{notas_50} notas de 50 reais')
    if notas_20 > 0:
        print(f'{notas_20} notas de 20 reais')
    if notas_10 > 0:
        print(f'{notas_10} notas de 10 reais')
    if notas_1 > 0:
        print(f'{notas_1} notas de 1 real')


    while not prosseguir:
        print('Deseja fazer outro saque ? [ Sim / Nao ]')
        mais = str(input('-> ')).upper().strip()[0]
        if mais == 'N':
            sair = True
        if mais == 'S' or mais == 'N':
            prosseguir = True
