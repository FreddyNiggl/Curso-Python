"""Leia o nome e a media de um aluno e guarde a sistuacao dele em um dicionario. no final,
 moste o conteudo da estruturaa tela"""

rendimento_escolar = {}
rendimento_escolar['aluno'] = str(input('Digite o nome do aluno: '))
rendimento_escolar['media'] = float(input('Qual a media do aluno: '))
if rendimento_escolar['media'] >= 7:
    rendimento_escolar['situacao'] = 'Aprovado'
else:
    rendimento_escolar['situacao'] = 'Reprovado'

print(f'O nome do aluno é: {rendimento_escolar['aluno']}')
print(f'A media do aluno foi: {rendimento_escolar['media']}')
print(f'A situacao dele na escola é: {rendimento_escolar['situacao']}')
