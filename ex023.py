# leia um numero de 0 - 9999 e mostre cada um deles separados
# unidade, dezena, centena, mulhar

print('Vamos separar alguns numero!')

# num0 = (int(input('Digite um numero de 0 - 9999: ')))
# num1 = '{}'.format(num0)
#
# print('O numero digitado foi: {}'.format(num1))
# if num1[-1]:
#       print('Sua unidade e: {}'.format(num1[-1]))
# if num1[-2] < 1:
#       print('Sua unidade de dezena e: {}'.format(num1[-2]))
# if num1[-3]:
#       print('Sua unidade de centena e: {}'.format(num1[-3]))
# if num1[-4]:
#       print('Sua unidade de milhar e: {}'.format(num1[-4]))


num = int(input('Digite um numero de 0 - 9999: '))
u = int(num // 1 % 10)
d = int(num // 10 % 10)
c = int(num // 100 % 10)
m = int(num // 1000 % 10)
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))