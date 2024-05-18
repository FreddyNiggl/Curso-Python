def arquivo_existe(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'rt')
        arquivo.close()
    except FileNotFoundError:
        print('Arquivo nao encotrado!')
        return False
    else:
        print('Arquivo visto')
        return True


def criar_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'wt+')
        arquivo.close()
    except:
        print('Problema na criacao do arquivo')
    else:
        print('Criacao de arquivo feita com sucesso!')


def leitura_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'rt')
    except:
        print('Nao consegui ler o arquivo')
    else:
        print('Leitura feita com sucesso!')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        arquivo = open(arq, 'at')
    except:
        print('Tivemos erro ao tentar abrir para cadastrar a nova pessoa')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('Problema para escrever nome e idade do cadastro')
        else:
            print(f'Cadastro de {nome} realizado com sucesso!')
