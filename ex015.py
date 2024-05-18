print('Hora de alguar carro!')
d = int(input('Por quanto tempo voce esteve com o carro alugado ? '))
km = float(input('Quantos km voce percorreu com o automovel alugado ? '))
custo = (d * 60) + (km * 0.15)

print('O custo a ser cobrado por dias é: {}\nO valor a ser cobrado por km rodados é: {}'
      '\nO valor total a ser pago é: {}'.format((d*60), (km*0.15), custo))