# programa que leia o nome e o preco de varios produtos.
# o program pergunta se o usuario deseja continuar no final
# no final mostr:
# qual o total gasto na compra
# quantos produtos custam mais de 1000 reais
# qual o nome do produto mais barato
print('*' * 20)
print('COMPRAS')
print('*' * 20)
nome_mais_caro = ''
produto_mais_caro = 0
produtos_1000reais = []
qt_1000reais = 0
total_gasto = 0
sair = False
continuar = False
while not sair:
    continuar = False
    print('Qual o nome do produto ? ')
    nome = str(input('-> ')).upper().strip()

    print('Qual o valor do produto ? ')
    custo = float(input('-> '))

    total_gasto = total_gasto + custo
    if total_gasto == 0:
        nome_mais_caro = nome
        produto_mais_caro = custo
    else:
        if custo > produto_mais_caro:
            nome_mais_caro = nome
            produto_mais_caro = custo
    if custo > 1000:
        produtos_1000reais.append((f'{nome}:', f'{custo:.2f}'))
        qt_1000reais += 1

    while not continuar:
        print('Deseja inserir outro produto ? [ Sim / Nao ] ')
        resp = str(input()).upper().strip()[0]
        if resp == 'S' or resp == 'N':
            continuar = True
        if resp == 'N':
            sair = True

print(f'A custo total da compra foi {total_gasto:.2f}')
print(f'A quantidade de produtos acima de 10000, reais e: {qt_1000reais}')
print(f'A lista dos produtos acima de 1000,00 reais e: {produtos_1000reais}')
print(f'O produto mais caro foi: {produto_mais_caro}')
