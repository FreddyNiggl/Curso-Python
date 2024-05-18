"""Crie uma lista e 2 funcoes. a 1 funcao vai sortear 5 numeros de dentro da lista e jogar na sgunda funcao
a segunda funcao por sua vez vai somar os numeros pares que foram recebidos da primeira funcao."""
import random


def sortear(*num):
    for i in range(0, 5):
        lista.append(random.randint(1, 10))
    print(lista)


def somar_pares(pares):
    soma = 0
    for k in pares:
        if k % 2 == 0:
            soma += k
    print(soma)
    # print(f'A soma dos numeros pares sorteados é: {soma}')




lista = []
sortear(lista)
somar_pares(lista)

