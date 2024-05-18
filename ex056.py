# ler nome, idade e sexo de 4 pessoas e no final mostrar
# a media da idade do grupo
# o nome do homem mais velho
# quantas mulheres tem menos de 20 anos
nome_homem_velho = ''
homem_velho = 0
mulheres_jovens = 0
idade_total = 0

numero_pessoas = int(input("Quantas pessoas tem o grupo ? "))

for i in range (0, numero_pessoas, 1):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = int(input('Qual seu sexo? \n'
                     '[ 1 ] - masculino\n'
                     '[ 2 ] - feminino\n  '))

    idade_total = idade_total + idade
    idade_media = idade_total / numero_pessoas

    if sexo == 2 and idade < 20:
        mulheres_jovens = mulheres_jovens + 1

    if sexo == 1 and idade > homem_velho:
        homem_velho = idade
        nome_homem_velho = nome

print('A media da idade do grupo eh: {}'.format(idade_media))
print('O numero de mulheres com idade < 20 anos eh: {}'.format(mulheres_jovens))
print('O nome do homem mais velho eh: {}'.format(nome_homem_velho))