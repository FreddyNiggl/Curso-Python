# refzer o desafio do triangulo mostrando dessa vez se o triangulo
# e equilatero, isosceles ou escaleno

print('Digite 3 valores de segmento do triangulo')
a = int(input('Digite o 1° segmento: '))
b = int(input('Digite o 2° segmento: '))
c = int(input('Digite o 3° segmento: '))

c1 = (a - b) < c < (a + b)
c2 = (c - b) < a < (c + b)
c3 = (a - c) < b < (a + c)

if c1 and c2 and c3 == True:
    print('Esse é um triangulo valido!')

    if a == b and b == c and c == a :
        print('triangulo equilatero')
    elif a != b and b != c and c != a:
        print('triangulo escaleno')
    else:
        print('triangulo isosceles')
else:
    print('\033[7;40mEsse não é um triangulo!\033[m')