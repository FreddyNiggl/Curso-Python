"""crie um programa que o ususario possa add varios valores numericos e cadastreos em uma lista
caso o numero ja esteja na lista o valor nao sera adicionado.
no final, sera exibido todos os valores unicos da lista em ordem crescente"""


lista = []
while True:
    print('Digite um numero: ')
    valor = int(input('-> '))
    cont = str(input('Deseja continuar ? [Sim / Nao]\n'
                     '-> ')).upper().strip()[0]
    if cont == 'N':
        break

    if valor not in lista:
        lista.append(valor)
    else:
        print(f'{valor} ja foi adicionado. Nao o farei de novo.')

print(lista)
print(sorted(lista))





