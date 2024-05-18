# calcular duas notas do aluno e dizer de menor que 5 reprovado.
# entre 5-6.9 recuperacao ou maior que 7 aprovado.

print('Hora das notas')

nota_1 = float(input('Qual o valor da 1° nota: '))
nota_2 = float(input('Qual o valor da 2° nota: '))

media = (nota_1 + nota_2) / 2

if media < 5:
    print('Te vejo ano que vem de novo. REPROVADO! Sua media eh {}'.format(media))
elif 5 <= media < 7:
    print('Te vejo na recuperacao. Sua media e {}'.format(media))
else:
    print('Parabens, APROVADO! Sua media e {}'.format(media))