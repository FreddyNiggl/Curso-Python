from ex115.funcoes import *
from ex115.arquivo_texto import *
import time

nome_arquivo = 'arquivo_cadastro.txt'
if not arquivo_existe(nome_arquivo):
    criar_arquivo(nome_arquivo)

while True:
    opcao = menu(['Ver lista', 'Cadastrar pessoa', 'Sair'])
    if opcao == 1:
        texto('PESSOAS CADASTRADAS...')
        leitura_arquivo(nome_arquivo)
    elif opcao == 2:
        texto('CADASTRANDO NOVA PESSOA')
        nome = str(input('NOME: '))
        idade = leiaint('IDADE: ')
        cadastrar(nome_arquivo, nome, idade)
    elif opcao == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('Erro! Valor invalido. Tente novamente.')
        time.sleep(2)
