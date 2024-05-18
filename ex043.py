# calcule o IMC e diga se a pessoa esta
# abaixo do peso-18.5
# peso ideal 18.5-25.0
# sobrepeso 25-30
# obesidade 30-40
# obesidade morbida +40

print('IMC')
peso = float(input('Qual seu peso atual ? '))
altura = float(input('Qual sua altura ? '))
imc = peso / pow(altura,2)

if imc < 18.5:
    print('Voce está abaixo do peso.')
elif 18.5 <= imc < 25.0:
    print('Voce está com o peso ideal')
elif 25 <= imc < 30:
    print('Voce está com sobrepeso')
elif 30 <= imc <= 40:
    print('Voce está com obesidade')
else:
    print('Voce esta com obesidade morbida')