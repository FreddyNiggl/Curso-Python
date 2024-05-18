# ler o numero de nascimento de 7 pessoas e dizer quantas ainda
# nao atingitam a maior idade e quantas ja atingiram 21anos
import datetime



pessoas = int(input('Quantas pessoas vao participar ? '))

maioridade = 0
minoridade = 0
for i in range(1, pessoas+1, 1):
    ano_nasc = int(input('Digite seu ano de nascimento'))
    ano_atual = datetime.date.today().year
    idade = ano_atual - ano_nasc
    if idade > 21:
        maioridade = maioridade + 1
    else:
        minoridade = minoridade + 1
print('O numero de pessoas menores de 21 anos eh: {}'.format((minoridade)))
print('O numero de pessoas maiores de 21 anos eh: {}'.format(maioridade))