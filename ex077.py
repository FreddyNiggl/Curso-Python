"""Crie uma tupla com varias palavras.
Depois disso para cada palavra voce deve mostrar suas vogais."""

tuplas = ()
for i in range(1, 5):
    print('Digite uma palavra: ')
    palavra = str(input('->  '))
    tupla = (palavra,)
    tuplas = tuplas + tupla

for j in range(0, len(tuplas)):
    vogais = ''
    for k in range(0, len(tuplas[j])):
        for m in tuplas[j][k]:
            if 'a' == tuplas[j][k]:
                vogais += 'a '
            if 'e' == tuplas[j][k]:
                vogais += 'e '
            if 'i' == tuplas[j][k]:
                vogais += 'i '
            if 'o' == tuplas[j][k]:
                vogais += 'o '
            if 'u' == tuplas[j][k]:
                vogais += 'u '

    print(f'As vogais de "{tuplas[j]}" são: {vogais.strip()}')










