"""crie um programa que recebe uma expressao matematica
e diga se a expressao esta com oas parenteses postos corretamente (valida) ou nao(invalida)"""


"""print('Entre com sua expressao matematica: ')
exp = str(input('-> '))
aberto = 0
fechado = 0
for i in range(0, len(exp), 1):
    for j in exp[i]:
        if j == '(':
            aberto += 1
        if j ==')':
            fechado += 1

if aberto == fechado:
    if i == 0 and j != '(':
        print('Sua expressao esta incorreta. Dica: olhe o inicio')
    if i == len(exp)-1 and j != ')':
        print('Sua expressao esta incorreta. Dica: olhe seu final')
    else:
        print('Expressao aceita com sucesso')
else:
    print('Expressao invalida')
"""

#########################################################################################

exp = str(input('Digite uma expressao: '))
pilha = []
for i in pilha:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressao valida')
else:
    print('Expressao invalida')