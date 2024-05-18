print('Hora do desconto!')
valor = float(input('Qual o preço da mercadoria que voce deseja comprar: '))
desc = valor - valor * 0.05
print('O valor anterior do produto era {}reais \nCom desconto de 5%, o produto agora vale: {:.2f}reais'
      .format(valor, desc))