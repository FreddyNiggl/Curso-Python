"""cire um programa que vai ler varios numero e coloca-ls em uma lista:
depois disso mostre:
quantos numeros forma digitados
a lista de valores ordenada de forma decrescente
se o valor 5 foi digitado e está na lista ou nao."""

lista = []
while True:
    print('Digite os valores: ')
    lista.append(int(input('-> ')))
    lista.sort(reverse=True)

    continuar = str(input('Deseja continuar inserindo valores ? ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Valor invalido. tente novamente')
        continuar = str(input('Deseja continuar inserindo valores ? ')).strip().upper()[0]
    if continuar == 'N':
        break


print(lista)
if 5 in lista:
    num_5 = lista.count(5)
    print(f'O numero 5 aparece {num_5} vezes')
else:
    print('O numero 5 nao aparece nenhuma vez na lisata')
