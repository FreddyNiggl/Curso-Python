# ler dois valores e mostrar um menu na tela
# 1  somar
# 2 multiplicar
# 3 qual o maior
# 4 novos numeros
# 5 sair do programa

resp = ''
while resp != 5:
    print('Digite dois numeros para fazermos algumas operações')
    num1 = int(input('1° numero:  '))
    num2 = int(input('2° numero:  '))

    print('O que deseja fazer??')
    print('-=' * 20)
    print('[ 1 ] - SOMAR ')
    print('[ 2 ] - MULTIPLICAR ')
    print('[ 3 ] - SABER QUAL O MAIOR ')
    print('[ 4 ] - MUDAR NUMEROS? ')
    print('[ 5 ] - SAIR')
    print('-=' * 20)
    resp = int(input('Sua escolha:  '))

    if resp == 1:
        print('A soma de {} + {} = {}'.format(num1, num2, num1 + num2))
    elif resp == 2:
        print('A multiplicacao de {} x {} = {}'.format(num1, num2, num1 * num2))
    elif resp ==3 :
        if num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
        elif num2 > num1:
            print('{} é maior que {}'.format(num2, num1))
        else:
            print('{} e {} são iguais'.format(num1, num2))
    elif resp == 4:
        print('Ok...vamos escolher novos numeros: ')
    elif resp == 5:
        print('Até mais seu cerebro de galinha haha...')
    else:
        print('Nem uma opcao consegue escolher?\n'
              'superistimei os seres humanos -_-')


print('Fim...')