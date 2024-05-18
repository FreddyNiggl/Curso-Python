# # leia um numero e mostre seu fatorial
# # ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
#
# resp = 0
# while resp != 2:
#     print('Digite o numero do qual precisa do fatorial, irei ajudar!')
#     resp = (int(input('Quer minha ajuda ? \n'
#                       '[ 1 ] - SIM\n'
#                       '[ 2 ] - NAO\n'
#                       'Sua resposta:  ')))
#     if resp == 1:
#         num = (int(input('Seu numero, por favor:   ')))
#         fat_soma = 1
#         if num == 0:
#             print('O fatorial de {} e = {} '.format(num, num))
#         else:
#             num_copy = num
#             while num > 0:
#                 print(' {} x'.format(num), end='')
#                 print(' x ' if num > 1 else ' = ', end='')
#                 fat_soma = fat_soma * num
#                 num = num - 1
#             print('\nO fatorial de {} e  = {} '.format(num_copy, fat_soma))
#     else:
#         print('Ate logo humano...')
# print('Fim...')


n = int(input('Digite um numero para calcular o  fatorial'))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))