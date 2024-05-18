# Crie um programa que lia a a idade e o sexo de varias pessoas
# a cada pessoa cadastrada, o progrmaa deve perguntar ao ussuario se quer continuar ou nao
# no final mostra:
# quantas pessoas tem mais de 18 anos
# quantos homens foram cadastrados
# quantas mulheres tem menos de 20 anos

print('*' * 20)
print('  REGISTRAR PESSOAS')
print('*' * 20)


contador_pessoas_mnais18 = 0
contador_homens = 0
contador_girl_menor20 = 0
contador_mulheres = 0
continuar = ''
prosseguir = False
sexo = 'g'
sexualidade = False
while continuar != 'N':
    prosseguir = False
    while not sexualidade:
        print('Registre aqui o sexo: [ M / F ]')
        sexo = str(input('-> ')).upper().strip()[0]

        if sexo == 'M' or sexo == 'F':
            sexualidade = True


    print('Registre aqui a idade: ')
    idade = int(input('->  '))


    if sexo == 'M':
        contador_homens += 1

    else:
        contador_mulheres += 1

    if idade > 18:
        contador_pessoas_mnais18 += 1

    if sexo == 'F' and idade < 20:
        contador_girl_menor20 += 1



    print(contador_homens)
    print(contador_mulheres)

    while not prosseguir:
        print('Deseja continuar registrando ? [ S / N ]')
        continuar = str(input(' ')).upper().strip()[0]
        sexualidade = False
        if continuar == 'S' or continuar == 'N':
            prosseguir = True



print(f'Foram cadastrado {contador_homens} homens.\n'
      f'Foram cadastrados {contador_pessoas_mnais18} pessoas com +18 anos.\n'
      f'Foram cadastradas {contador_girl_menor20} de mulheres menores de 20 anos.')