def aumentar(preco, taxa):
    valor = (preco * (taxa/100)) + preco
    return valor


def diminuir(preco, taxa):
    valor = -(preco * (taxa/100)) + preco
    return valor


def dobro(preco):
    valor = 2 * preco
    return valor


def metade(preco):
    valor = preco / 2
    return valor


