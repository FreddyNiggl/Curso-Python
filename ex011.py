print('Vamos pintar uma parede!')
h = float(input('Qual a altura da parede que deseja pintar (metros) ?'))
l = float(input('QUal a largura da parede que deseja pintar (metros) ?'))
A = h * l
tinta_litros = A/2

print('A quantidade de tinta para pintar uma parede de altura {}m e largura {}m é: {}litros'
      .format(h,l,tinta_litros))