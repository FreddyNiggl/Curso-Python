# leia um numero N qualuqer e mostre N primeiros
# numeros de uma sequencia de fibonacci

contador = 1
numero = ''
while numero != contador:
    print('Quantos numero voce deseja na tabela de fibonacci ? ')
    numero = int(input('Sua resposta: '))
    fibo = [0, 1]

    for i in range(1, numero - 1, 1):
        novo_numero = fibo[i] + fibo[i - 1]
        fibo.append(novo_numero)
        contador = contador + 1
    print(fibo)
    print(type(fibo))
