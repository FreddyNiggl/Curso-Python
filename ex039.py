# pegar a idade do usuario e dizer que ele ainda vai ter de se alistar,
# se ja está na hjora de se alistar ou se ainda vai se alistar.
# mostrar o tempo que falta ou que ja se passou tbm.
import datetime
print('Hora de se alistar')
nasc = int(input('Em que ano voce nasceu?'))
ano_atual = datetime.date.today().year
idade = ano_atual - nasc

if idade < 18:
    tempo = -idade + 18
    print('Faltam {} anos para voce se alistar'.format(tempo))
elif idade > 18:
    tempo = idade - 18
    print('Voce ja deveria ter se alistado. Ja se passou {} anos'.format(tempo))
else:
    print('\033[4mSeja bem vindo!\033[m Esse ano é seu ano de alistamento!')