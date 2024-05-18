import random

print('Hora de apresentar os trabalho !')

print('Alunos se apresentem:!')
a1 = str(input('Qual o nome do 1° aluno ? '))
a2 = str(input('Qual o nome do 2° aluno ? '))
a3 = str(input('Qual o nome do 3° aluno ? '))
a4 = str(input('Qual o nome do 4° aluno ? '))

sortudos = [a1, a2, a3, a4]
random.shuffle(sortudos)
print('A ordem dos alunos será: {}'.format(sortudos))



# a = random.choice(sortudos)
# sortudos.remove(a)
#
# b = random.choice(sortudos)
# sortudos.remove(b)
#
# c = random.choice(sortudos)
# sortudos.remove(c)
#
# d = random.choice(sortudos)

# print('O 1° sortudo eh: {}; \nO 2° sortudo eh: {}; \nO 3° sortudo eh: {} \nO 4° sortudo eh: {}'
#       .format(a, b, c, d))
