# ler o peso de 5 pessoas e no final dizer qual foi o mais pesado e o menos pesado

pessoas = int(input('Quantas pessaos vao participar ? '))

menos_gordo = 9999
mais_gordo = 0
for i in range(1, pessoas, 1):
    peso = float(input('Qual o seu peso?'))
    if peso > mais_gordo:
        mais_gordo = peso
    if peso < menos_gordo :
        menos_gordo = peso
print('O maior peso foi: {}'.format(mais_gordo))
print('O menor peso foi: {}'.format(menos_gordo))

