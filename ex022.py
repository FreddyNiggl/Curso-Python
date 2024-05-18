print('Bora analisar um nome?')

frase = str(input('Digite seu nome completo aqui:')).strip()
mai = frase.upper()
min = frase.lower()

letras_totais = len(frase) - frase.count(' ')

separar_frase = frase.split()
n_letras_nome1 = len(separar_frase[0])

print('Nome em maiusculo: {}\n'
      'Nome em minusculo: {}\n'
      'Numero de letrs sem espaco: {}\n'
      'Numero de letras do primeiro numero {}'.format(mai, min, letras_totais, n_letras_nome1))

