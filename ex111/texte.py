"""Crie um modulo chamado moeda.py com funcoes:
aumentar()
diminuir()
dobro()
metade()
Faca tbm um programa que importe esse modulo e utilize as funcoes do modulo"""
from ex111.utilidadescev import dados
from ex111.utilidadescev import moeda

p = dados.leiadado('Digite um valor:\n -> ')
# print(f'O dobro de {moeda.moeda(p)} é {(moeda.dobro(p, True))}')
# print(f'A metade de {moeda.moeda(p)} é {(moeda.metade(p, True))}')
# print(f'Aumentando 15% de {moeda.moeda(p)} temos {(moeda.aumentar(p, 15, True))}')
# print(f'Diminuindo 10% de {moeda.moeda(p)} temos {(moeda.diminuir(p, 10, True))}')
moeda.resumo(p, 35, 12, True)
