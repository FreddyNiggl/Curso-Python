"""o usuario possa cadastrar 5 valores numericos e cadastre-os em uma lista,
ja na posicao correta de insercao sem utilizar o 'sort'. NO final, mostre a lista ordenada"""

valores = []
for i in range(0, 11):
    print('Digite um numero: ')
    valor = int(input('-> '))
    if i == 0 or valor > valores[-1]:
        valores.append(valor)
    else:
        contador = 0
        while contador < len(valores):
            if valor <= valores[contador]:
                valores.insert(contador, valor)
                break
            contador += 1
print(valores)




