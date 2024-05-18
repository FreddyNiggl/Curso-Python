def moeda(preco=0.0, moeda='RS'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def aumentar(preco=0, taxa=0, format=False):
    valor = (preco * (taxa/100)) + preco
    if format:
        return moeda(preco=valor)
    else:
        return valor


def diminuir(preco=0, taxa=0, format=False):
    valor = -(preco * (taxa/100)) + preco
    if format:
        return moeda(valor)
    else:
        return valor


def dobro(preco=0, format=False):
    valor = 2 * preco
    if format:
        return moeda(valor)
    else:
        return valor


def metade(preco=0, format=False):
    valor = preco / 2
    if format:
        return moeda(valor)
    else:
        return valor


