# ler o comprimento de 3 retas e dizer se um triangulo pode ser formado

print('Digite 3 valores de segmento do triangulo')
a = int(input('Digite o 1° segmento: '))
b = int(input('Digite o 2° segmento: '))
c = int(input('Digite o 3° segmento: '))

c1 = (a - b) < c < (a + b)
c2 = (c - b) < a < (c + b)
c3 = (a - c) < b < (a + c)

if c1 and c2 and c3 == True:
    print('Esse é um triangulo valido!')
else:
    print('\033[7;40mEsse não é um triangulo!\033[m')