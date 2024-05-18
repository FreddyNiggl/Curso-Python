# leia um ano qualquer e diga se ele é ano bissexto ou nao
import datetime
ano = int(input('Digite um ano para descobrir se ele é bissexto: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0  or ano % 400 == 0 :
    print('{} Esse é um ano bissexto!'.format(ano))
else:
    print('{} Esse não é um ano bissexto'.format(ano))
