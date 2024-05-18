def leiaint():
    try:
        numero = str(input('Digite valor: '))
        numero.isnumeric()
        numero = int(numero)
        print(f'O valor inserido foi validado como sendo: {numero}')
    except KeyboardInterrupt:
        numero = 0
        print(numero)
        print(f'Erro! O cliente preferiu nao inserir o valor')
    except ValueError:
        if numero == '':
            numero = int(0)
            print(f'Erro de valor encontrado. \'{numero}\' não aceito como sendo um NUMERO INTEIRO')
        else:
            print(f'Erro de valor encontrado. \'{numero.strip()}\' não aceito como sendo um NUMERO INTEIRO')
    finally:
        print('Obrigado por experimentar nosso programa. Volte sempre.')


def leiafloat():
    try:
        numero = str(input('Digite valor: ')).replace(',', '.')
        numero = float(numero)
        print(f'O valor inserido foi validado como sendo: {numero}')
    except KeyboardInterrupt:
        numero = 0
        print(numero)
        print(f'Erro! O cliente preferiu nao inserir o valor')
    except ValueError:
        if numero == '':
            numero = int(0)
            print(f'Erro de valor encontrado. \'{numero}\' não aceito como sendo um NUMERO FLOAT')
        else:
            print(f'Erro de valor encontrado. \'{numero.strip()}\' não aceito como sendo um NUMERO FLOAT')
    finally:
        print('Obrigado por experimentar nosso programa. Volte sempre.')


def leiainteiro(txt):
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
