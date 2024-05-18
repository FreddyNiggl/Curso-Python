#pergunta o valor da casa, qual o salario e em quanto tempo a pessoa deseja parcelar
# a parcela nao pode ser maior que 30% do salario do comprador
# Qual o valor da prestacao mensal. se maior que 30%, financiamento negado
print('Vamos comprar uma casa')

v_casa = float(input('Qual o valor da cada?'))
v_salario = float(input('QUal o valor do seu salario?'))
parcelas = int(input('Em quantas parcelas deseja pagar?'))

v_salario_parcela = v_salario * 0.30
parcelas_per = v_casa // v_salario_parcela
n_meses = v_casa // parcelas

if parcelas > parcelas_per:
    print('O numero de parcelas excede o permitido, financiamento \033[1;31mnegado\033[m')
    print('O numero maximo de parcelas permitidas eh {}'.format(parcelas_per))
elif parcelas < parcelas_per:
    print('\033[1;32mFinanciamento aprovado!\033[m O pagamento total se dará em {} parcelas'.format(parcelas))