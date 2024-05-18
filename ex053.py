# ler uma frase e dizer se ela e um polindromo, desconsiderando os espacos.

frase = str(input('Digite sua frase: ')).upper().strip().split()
frase = (''.join(frase))
# print(frase)
frase_invertida = frase[::-1]
# print(frase)
# print(len(frase))
c = -1
gemeos = ''
for i in range(0, len(frase)):
    if frase[i] == frase_invertida[c]:
        gemeos = gemeos + frase[i]
        print('{} é = {}'.format(frase[i], frase_invertida[c]))
        c = c -1
    else:
        c = c -1

if gemeos == frase:
    print('São polindromo!')
    # print(gemeos)
else:
    print('Nao sao polindromos!')

print('Fim...')
