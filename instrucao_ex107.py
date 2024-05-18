"""Crie um modulo chamado moeda.py com funcoes:
aumentar()
diminuir()
dobro()
metade()
Faca tbm um programa que importe esse modulo e utilize as funcoes do modulo"""
import moeda

p = float(input('Digite um valor:\n -> '))
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'Aumentando 15% de {p} temos {moeda.aumentar(p)}')
print(f'Diminuindo 10% de {p} temos {moeda.diminuir(p)}')


