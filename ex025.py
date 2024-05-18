# Leia o nome de uma pessoa e diga se ela possui o nome SILVA dentro do nome

print('Procurar nome:')

nome = str(input('Digite seu nome:'))
nome_M = nome.upper()
achar = 'SILVA' in nome_M

print('O nome possui SILVA em alguma parte ? {}'.format(achar))