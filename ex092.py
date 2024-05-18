"""Crie um progrma que leia o nome, o ano de nascimento e a carteira de trabalho.
cadastre-os com idade em um dicionario.
Se por acaso o CTPS for diferente de 0, O dicionario recebera tbm o ano de contratacao do funcioaneeio e o salario
calcule e acrescente, alem da idadde, com quantos anos a pessoa vai se aposentar"""
import datetime

dici_trabalho = {}
year = datetime.date.today().year
dici_trabalho['nome'] = str(input('Digite seu nome: '))
ano_nasc = int(input('Seu ano de nascimento: \n'
                     '-> '))
dici_trabalho['idade'] = year - ano_nasc
trabalha = str(input('Possui carteira de trabalho ? [S/N]'))

if trabalha in 'Ss':
    dici_trabalho['cart_trabalho'] = 'SIM'
    print(f'O valor do campo nome e: {dici_trabalho['nome']}')
    print(f'O valor do campo idade e: {dici_trabalho['idade']}')
    print(f'O valor do campo carteira de trabalhoe: {dici_trabalho['cart_trabalho']}')
    print(f'O valor do campo ano de contrato: {dici_trabalho['ano_contrat']}')
    print(f'O valor do campo salario: {dici_trabalho['salario']}')
    print(f'O valor do campo aposentadoria: {dici_trabalho['aposentar']}')
else:
    dici_trabalho['cart_trabalho'] = 'NAO'
    print(dici_trabalho)
    print(f'O valor do campo nome e: {dici_trabalho['nome']}')
    print(f'O valor do campo idade e: {dici_trabalho['idade']}')
    print(f'O valor do campo carteira de trabalhoe: {dici_trabalho['cart_trabalho']}')
dici_trabalho['ano_contrat'] = int(input('Em que ano assinou a carteira ?\n -> '))
dici_trabalho['salario'] = float(input('Qual o salario ? \n -> '))
dici_trabalho['aposentar'] = (- ((year - dici_trabalho['ano_contrat']) - 35)) + dici_trabalho['idade']

print(dici_trabalho)

