def moeda(preco=0.0, moeda='RS'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def aumentar(preco=0, taxa=0, formato=False):
    valor = (preco * (taxa/100)) + preco
    if formato:
        return moeda(preco=valor)
    else:
        return valor


def diminuir(preco=0, taxa=0, formato=False):
    valor = -(preco * (taxa/100)) + preco
    if formato:
        return moeda(valor)
    else:
        return valor


def dobro(preco=0, formato=False):
    valor = 2 * preco
    if formato:
        return moeda(valor)
    else:
        return valor


def metade(preco=0, formato=False):
    valor = preco / 2
    if formato:
        return moeda(valor)
    else:
        return valor


def resumo(preco, taxa1, taxa2, formato):
    frase = 'RESUMO DO VALOR'
    print(f'~' * (len(frase)+8))
    print(f'    {frase}')
    print(f'~' * (len(frase)+8))
    print(f'{"PRECO ANALISADO:"}\t\t{moeda(preco)}')
    print(f'{"DOBRO DO PRECO:"}\t\t\t{dobro(preco, formato)}')
    print(f'{"METADE DO PRECO:"}\t\t{metade(preco, formato)}')
    print(f'{taxa1}{"% de Aumento:"}\t\t\t{aumentar(preco, taxa1, formato)}')
    print(f'{taxa2}{"% de Desconto:"}\t\t{diminuir(preco, taxa2, formato)}')


