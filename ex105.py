"""Faca um programa que tenha a funcao NOTAS() que pode receber varias notas de varios alunos e
vai retornar um dicionario com as seguintes informacoes:
qunatidade de notas
a maior nota
a menor nota
a media da turma
a situacao(opcional)
- add a docstring dafuncao"""


def status(*num, sit=False):
    """Funcao para calcular status de uma sala baseado nas notas dos seus alunos.
    :param num: notas doas alunos.
    :param sit: Deseja ver a situacao da sala?.
    :return: retorna objeto classe com parametros preenchidos.
    """
    classe = {}
    classe['total'] = len(*num)
    classe['maior'] = max(*num)
    classe['menor'] = min(*num)
    soma = sum(*num)
    classe['media'] = soma / len(*num)
    if sit:
        if 5 <= classe['media'] < 6:
            classe['situacao'] = 'Razoavel'
        elif 5 > classe['media']:
            classe['situacao'] = 'Ruim'
        elif classe['media'] >= 6:
            classe['situacao'] = 'BOA'
    return classe


notas = []
while True:
    notas.append(float(input('Digite uma nota:\n-> ')))
    cont = str(input('Deseja continuar inserindo notas? [S / N]')).upper().strip()[0]
    if cont in 'Nn':
        break
situacao = str(input("Deseja ver a situacao da classe ?\n-> [True / False]").upper().strip()[0])
while situacao not in 'FT':
    print('Entrada invalida. Tente de novo')
    situacao = str(input("Deseja ver a situacao da classe ?\n-> [True / False]").upper().strip()[0])
    if situacao == 'F':
        situacao = False
    else:
        situacao = True

classe = status(notas, sit=situacao)
print(f'O status da classe é: {classe}')
# help(status)