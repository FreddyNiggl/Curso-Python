import math

print('Hora dos sen, cos, tg kkkkk')

ang = float(input('Digite o angulo cuja deseja saber os valores de SEN, COS e Tg: '))

# rad = ang * math.pi / 180
# cos = math.cos(rad)
# sen = math.sin(rad)
# tg = math.tan(rad)
# c = math.sqrt(2)/ 2
cos = math.cos(math.radians(ang))
sin = math.sin(math.radians(ang))
tg = math.tan(math.radians(ang))

print('O valor do cosseno do angulo {}, é {:.2f};\n'
      'O valor do seno do angulo {}, é {:.2f};\n'
      'O valor da tangente do angulo {}, é {:.2f}'.format(ang,cos,ang,sin,ang,tg))