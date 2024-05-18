# calcule o valor a ser pago de um produto considerando a froma de pgaamento
# avista ou cheque 10% desconto
# avista cartao 5% desconto
# 2x no cartao preco normal
# 3x + no cartao  20% de juros

print('Pague nao deva')
preco = float(input('Qual o preco do produto ? '))
pag = int(input('Qual a forma de pagamento ? \n'
                'Digite 1 p/ avista ou cheque(-10%) \n'
                'Digite 2 p/ avista com cartao (-5%) \n'
                'Digite 3 p/ 2x no cartao (sem desconto) \n'
                'Digite 4 p/ +2x no cartao (+20%) '))
avista = preco - preco * 0.10
avista_card = preco - preco * 0.05
card_2x = preco
card_xx = preco + preco * 0.20

if pag == 1:
    print('O preco a se pagar eh {} '.format(avista))
elif pag == 2:
    print('O preco a se pagar eh {} '.format(avista_card))
elif pag == 3:
    print('O preco a se pagar eh {} '.format(card_2x))
elif pag == 4:
    print('O preco a se pagar eh {} '.format(card_xx))
else:
    print('Opcao invalida. Por favor selecione uma opcao valida.')