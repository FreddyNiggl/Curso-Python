"""Crie um programa que leia o nome de alunos e guarde 2 notas  tudo em uma lista composta
no final mostre o boletim contendo a media  de cada aluno e permita que o ususario possa
mostrar a media de cada aluno indivivdualmente."""
lista_completa = []
lista_alunos = []
lista_notas = []
lista_media = []

while True:
    print('Qual o nome do aluno que deseja cadastrar ? ')
    nome = str(input('-> '))
    lista_alunos.append(nome)

    nota_1 = float(input('Qual foi a 1° nota dele ?\n'
                         '-> '))
    nota_2 = float(input('Qual foi a 2° nota dele ?\n'
                         '-> '))
    lista_notas.append(nota_1)
    lista_notas.append(nota_2)

    media = f'{(nota_1 + nota_2) / 2:.2f}'
    lista_media.append(media)

    lista_alunos.append(lista_notas)
    lista_alunos.append(lista_media)
    lista_completa.append(lista_alunos)
    lista_alunos = []
    lista_notas = []
    lista_media = []

    continuar = str(input('Deseja continuar ? ')).strip()
    while continuar not in 'SsNn':
        print('Entrada invalida. Tente novamente')
        continuar = str(input('Deseja continuar ? ')).strip()
    if continuar in 'Nn':
        break
print(lista_completa)

print('-=' * 40)
print('No.  NOME         MEDIA')
print('_' * 26)

for i in range(0, len(lista_completa), 1):
    print(f'{i:<5}{lista_completa[i][0]:<15}{lista_completa[i][2][0]:>}')

while True:
    print('Deseja ver as notas de algum aluno ? [S / N]')
    resp = str(input('-> '))
    while resp not in 'SsNn':
        print('Valor invalido. Tente novamente.')
        print('Deseja ver as notas de algum aluno ? [S / N]')
        resp = str(input('-> '))
        if resp in 'nN':
            break

    print('De qual alunos voce deseja ver ? (N° do aluno)')
    num_aluno = int(input('-> '))
    while num_aluno > len(lista_completa)-1:
        print('Valor invalido. Tente novamente.')
        print('De qual alunos voce deseja ver ? (N° do aluno)\n'
              '(999 para sair)')
        num_aluno = int(input('-> '))
        if num_aluno == 999:
            print('Ate logo!')
            break

    print(f'Nota 1 = {lista_completa[num_aluno][1][0]}')
    print(f'Nota 2 = {lista_completa[num_aluno][1][1]}')


