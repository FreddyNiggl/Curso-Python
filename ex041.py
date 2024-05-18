# calcular a idade de um atleta e dizer em qual categoria ele
# esta. 9 ano mirim, 14 -infantil, 19-junior, 20-senior, acima - master

idade = int(input('Qual sua idade??'))

if 9 <= idade <14 :
    print('Mirim')
elif 14 <= idade < 19:
    print('Infantil')
elif 19 <= idade < 20:
    print('Senior')
elif 20 == idade:
    print('Senior')
elif 20 < idade:
    print('Master')