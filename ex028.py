# Faca o computador escolher um numero entre 0-5
# e peca para o usuário adivinhar e dizer se acertou ou nao.
import random

entrar = 's'
while entrar == 's':
    sorteio = random.randint(1,5)
    print(sorteio)
    print('PC...escolhi um numero entre 1 e 5. Tente adivinhar se for capaz!')

    n = int(input('Que numero voce acha que o computador escolheu ?'))
    if n == sorteio:
        print('Voce venceu! Derrotou o computador! uau')
        entrar = 'n'
    else:
        print('Voce foi derrotado como muitos outros... '
                  'Eu soube desde o inicio que nao havia nada de especial em voce')
# entrar = str(input('deseja continuar??'))