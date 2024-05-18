# usuario escreve um numero e escolhe a base de conversao entre binario, octal, hexadecimal

print('Converter numero!')
op2 = 'NAO'
while op2 != 'SIM':
    num = int(input('Qual numero deseja converter ? '))

    print('Escolha um tipo de conversao: ')
    op = int(input('Digite 1 para conversao BINARIA: \n'
                   'Digite 2 para conversao OCTAL: \n'
                   'Digite 3 para conversao HEXADECIMAL: \n'))

    if op == 1:
        print('{} convertido para binario eh = {}'.format(num, bin(num)[2:]))
    elif op == 2:
        print('{} convertido para OCTAL eh = \033[1;34m{}\033[m'.format(num, oct(num)[2:]))
    elif op == 3:
        print('{} convertido para HEXADECIMAL eh = {}'.format(num, hex(num)[2:]))
    else:
        print('Opccao invalida. Por favor escolha uma das opcoes acima.')

    op2 = str(input('Deseja sair? sim ou nao? ')).upper().strip()