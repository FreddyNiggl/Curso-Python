# refazer o ex 51 com while.
#     ler 1° termo, ler a razao e mostrar  os 10 primeiros numeros da PA

print('Vou te ajudar com essa PA. Me diga qual o 1° termo e qual a razao.')
termo_1 = (int(input('1° Termo: ')))
razao = int(input('Qual a razao da PA: '))
termo_x = (int(input('Quantos termos voce deseja?')))
continuar = 1
contador = 1
while continuar != 2:
    while termo_x != contador-1:
       if contador == 1:
           print('O {}° termo dessa PA é {}'.format(contador, termo_1))
       numero = razao * contador + termo_1
       print('O {}° termo dessa PA é {}'.format(contador, numero))
       contador = contador + 1

    print('Voce precida de mais numeros?')
    continuar = int(input('[ 1 ] - SIM\n'
                        '[ 2 ] - NAO\n'
                          'Sua escolha:  '))
    if continuar == 1:
        termo_x = (int(input('Quantos termos voce deseja?')))