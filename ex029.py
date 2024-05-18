# O programa vai ler a velocidade do carro
# se for acima de 80km/h o motorista sera multado
# cada km acima do limite custa 7 reais

vel = float(input('Qual a velocidade do carro?'))

if vel > 80:
    print('Voce foi multado!')
    multa = (vel - 80) * 7
    print('Sua multa é de {:.2f}reais'.format(multa))
else:
    print('Parabens, voce é um motorista responsável.')