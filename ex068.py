# jogue par ou impar contra o computador. O programa so sera interrompido quando o ususraio perder
# mostrando a sequencia de vitorias dele.
import random

print('#' * 20)
print('   ~PAR OU IMPAR~')
print('#' * 20)
vitoria = 0
derrota = False
resultado = ''
while not derrota:
    pc_num = random.randint(1, 10)
    print('Esoclha um numero a se jogar:')
    user_num = int(input('->  '))
    print('Quer apostar em Par ou Impar ? [ P / I ]')
    aposta = str(input('->  ')).upper().strip()[0]
    if aposta not in 'PpIi':
        print('Opcao invalida, escolha uma opcao valida.')
    else:
        soma = user_num + pc_num
        resultado = soma
        if soma % 2 == 0:
            soma = aposta
            if aposta == 'P':
                print(f'Voce venceu! O resultado foi {resultado} um numero par')
                vitoria = vitoria + 1
            else:
                print(f'Voce perdeu! O resultado foi {resultado} um numero par')
                derrota = True
        else:
            soma = aposta
            if aposta == 'I':
                print(f'Voce venceu! O resultado foi {resultado} um numero impar')
                vitoria = vitoria + 1
            else:
                print(f'Voce perdeu! O resultado foi {resultado} um numero impar')
                derrota = True
print(f'Teve um total de {vitoria} vitorias consecutivas')