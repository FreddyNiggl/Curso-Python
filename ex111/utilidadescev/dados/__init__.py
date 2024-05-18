def leiadado(msg):
    while True:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! \"{entrada}\" Valor invalido. Tente novamente\033[m')
        else:
            return float(entrada)
