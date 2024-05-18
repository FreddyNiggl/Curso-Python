# pergunta a distancia da viagem e cobra 0.50 por km de viagens ate 200km
# e 0.45/km por viagens mais longas

viagem = float(input('Qual a distancia da viagem que deseja fazer??'))
if viagem > 200:
    valor = viagem * 0.45
    print("O valor da sua passagem custa {}reais".format(valor))
    print('O custo do km eh 0.45 ')
else:
    valor = viagem * 0.50
    print('O valor da sua passagem custa {}reais'.format(valor))
    print('O custo do km eh 0.50 ')



# preco = viagem * 0.50 if viagem <= 200 else viagem * 0.45