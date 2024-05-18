# crie um programa que faca o computador jogar jokempo contra voce
import random
import time

print('Estou escolhendo...')

jp = random.randint(1, 3)
vc = int(input('Escolha 1 para TESOURA, 2 para PAPEL e 3 para PEDRA.'))
print('Estou pronto.')
print('Voce está pronto?')
time.sleep(1)
print('3...')
time.sleep(1)
print('2...')
time.sleep(1)
print('1...')
time.sleep(1)
print('go!!')

if jp == 1:
    print(' =        =\n'
          '  =      =\n'
          '   =    =\n'
          '    =  =\n'
          '     ==\n'
          '   =    =\n'
          '|==|    |==|\n'
          '|==|    |==|\n'
          '  (TESOURA)')
elif jp == 2:
    print('|=============|\n'
          '|=============|\n'
          '|=============|\n'
          '|=============|\n'
          '|=============|\n'
          '    (FOLHA)')
else:
    print(
          '  XXXXXXX\n '
          ' XXXXXXXXX\n'
          'XXXXXXXXXXX\n'
          'XXXXXXXXXXX\n'
          ' XXXXXXXXX\n'
          '  XXXXXXX\n'
          '  (PEDRA)')

print('\033[36m-=\033[m' * 20)
print('')
print('\033[36m-=\033[m' * 20)




if vc == 1:
    print(' =        =\n'
          '  =      =\n'
          '   =    =\n'
          '    =  =\n'
          '     ==\n'
          '   =    =\n'
          '|==|    |==|\n'
          '|==|    |==|\n'
          '  (TESOURA)')
elif vc == 2:
    print('|=============|\n'
          '|=============|\n'
          '|=============|\n'
          '|=============|\n'
          '|=============|\n'
          '    (FOLHA)')
else:
    print(
          '  XXXXXXX\n '
          ' XXXXXXXXX\n'
          'XXXXXXXXXXX\n'
          'XXXXXXXXXXX\n'
          ' XXXXXXXXX\n'
          '  XXXXXXX\n'
          '  (PEDRA)')

time.sleep(1)

if jp == 1 and vc == 3:
    print('\033[32mVoce venceu\033[m')
elif jp == 1 and vc == 2:
    print('\033[31mVoce perdeu\033[m')
elif jp == 1 and vc == 1:
    print('\033[7;40mEmpate\033[m')
elif jp == 2 and vc == 3:
    print('\033[31mVoce perdeu\033[m')
elif jp == 2 and vc == 2:
    print('\033[7;40mEmpate\033[m')
elif jp == 2 and vc == 1:
    print('\033[32mVoce venceu\033[m')
elif jp == 3 and vc == 3:
    print('\033[7;40mEmpate\033[m')
elif jp == 3 and vc == 2:
    print('\033[32mVoce venceu\033[m')
elif jp == 3 and vc == 1:
    print('\033[31mVoce perdeu\033[m')
else:
    print('Alguma coida deu errado kkkk')
