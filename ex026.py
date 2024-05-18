# leia uma frase, diga quantas letras A nela possui e diga a posicao do 1 A e do ultimo A

print('Contar letras em uma frase:')

frase = 'Sabrina Marques'.upper().strip()

letra = str(input('Digite a letra que deseja encontrar: ')).upper().strip()

qt = frase.count(letra)
posi = frase.find(letra) + 1
posi2 = frase.rfind(letra) + 1

print('Quantas letras: "{}" tem na frase "{}" ?\n'
      'A quantidade de letras "{}" e: {}\n'
      'A posicao da 1° letra "{}" e {}'.format(letra, frase, letra, qt, letra, posi))
print('A posicao da ultima letra "{}" e: {}'.format(letra, posi2))