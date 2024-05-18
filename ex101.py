"""Crie uma funcao chamada de VOTO() que vai receber um parametro (O ANO DE NASCIMENTO)
de uma pessoa. Retornando um valor literal indicando se a pessoa tem voto de NEGADO, OPCIONAL ou OBRIGATORIOS
as eleicoes"""
import datetime

def voto():
    ano_atual = datetime.date.today().year
    ano_nascimento = int(input('Em que ano voce nasceu ?\n -> '))
    idade = ano_atual - ano_nascimento
    if idade < 18:
        print('Voto: NEGADO')
    elif 18 <= idade <65:
        print('Voto: OBRIGATORIO')
    else:
        print('Voto: OPCIONAL')

voto()