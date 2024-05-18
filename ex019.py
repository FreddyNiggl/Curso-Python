import random

print('Bora apagar esse quadro hehehe')

print('Alunos se apresentem:!')
a1 = str(input('Qual o nome do 1° aluno ? '))
a2 = str(input('Qual o nome do 2° aluno ? '))
a3 = str(input('Qual o nome do 3° aluno ? '))
a4 = str(input('Qual o nome do 4° aluno ? '))

alunos = [a1, a2, a3, a4]
sortudo = random.choice(alunos)

print('O aluno sortudo kkkk foi: {}'.format(sortudo))
