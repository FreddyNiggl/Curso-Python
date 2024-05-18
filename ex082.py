"""crie um progrma para ler varios numeros e colcoar na lista
depois disso, crie duas listas extras que vao conter apenas os valores pares
e a outra os impares
no final mostre o conteudo das 3 listas"""
lista = []
while True:
    print('Digite os valores desejados: ')
    lista.append(int(input('-> ')))
    lista.sort(reverse=True)

    continuar = str(input('Deseja continuar? [Sim / Nao]\n'
                          '-> ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Entrada errada, tente novamente...')
        continuar = str(input('Deseja continuar? [Sim / Nao]')).strip().upper()[0]
    if continuar == 'N':
        break

lista_par = []
lista_impar = []
for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
        lista_par.sort()
    else:
        lista_impar.append(i)
        lista_impar.sort()

print(f'Todos valores digitados: {lista}')
print(f'Todos valores digitados pares: {lista_par}')
print(f'Todos valores digitados impares: {lista_impar}')

