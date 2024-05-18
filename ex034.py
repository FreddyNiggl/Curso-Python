# pergunta o salario de um funcionariio e calcula seu aumento
# salarios maiores que 1250 aumento de 10%
# para inferiores ou iguais o aumento é de 15%

sal = float(input('Qual seu salario?'))

aument1 = sal + sal * 0.15
aument2 = sal + sal * 0.10

if sal <= 1250:
    print('Seu novo salario a partir de agora sera de: {}'.format(aument1))
else:
    print('-='*20)
    print('\033[7;40mSeu novo salario a partir de agora sera de: {}\033[m'.format(aument2))
    print('\033[1;35m-=' * 25)
