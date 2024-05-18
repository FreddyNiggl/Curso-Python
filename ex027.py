# Leia o nome de uma pessoa e mostre depois qual o primeiro nome e o ultimo nome de forma separada

print('Descobrir Nome e Sobrenome:')

nome = str(input('Digite seu nome completo aqui: '))
nome_split = nome.split()

print('O primeiro nome e: {}\n'
      'O Sobrenome e: {}'.format(nome_split[0], nome_split[-1]))