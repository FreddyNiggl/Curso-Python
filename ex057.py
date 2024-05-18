sexo = ''
while sexo != 'F' and sexo != 'M':
    print('Digite seu respectivo sexo de acordo com a tabela.')
    print('-=' * 20)
    print('[ F ] - MASCULINO\n''[ M ] - FEMININO')
    print('-=' * 20)
    sexo = str(input('Resposta: ')).upper().strip()

    if sexo not in 'MF':
        print('\033[31mEntrada invalida, por favor selecione uma opcao válida.\033[m')

print('FIM...')
