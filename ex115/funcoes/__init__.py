def leiaint(txt):
    while True:
        try:
            numero = int(input(txt))
        except (ValueError, TypeError):
            print('Valor digitado nao é um tipo INTEIRO')
        except KeyboardInterrupt:
            print('Usuario interrompeu a entrada de dados')
            return 0
        else:
            return numero


def linha(lin=42):
    print('~' * lin)


def texto(txt):
    linha()
    print(txt.center(42))
    linha()


def menu(lista):
    texto('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    linha()
    return leiaint('Sua opção: ')
