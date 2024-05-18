import math

print('Hora dos triangulos retangulos!')

cat1 = float(input('Digite a medida do 1° cateto: '))
cat2 = float(input('Digite a medida do 2 ° cateto: '))
# v1 = math.pow(cat1, 2)
# v2 = math.pow(cat2, 2)
# hip = math.sqrt(v1 + v2)
hip = math.hypot(cat1, cat2)

print('O valor da hipotenusa é: {:.2f} '.format(hip))
