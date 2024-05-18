frase = 'Curso em Video Python'
print(frase[-1])
print(frase[5:])
print(frase[:9])
print(frase[1:15:3])
print(frase[3::2])
print(len(frase))
print(frase.count('o'))
print(frase.count('o',2,15))
print(frase.find('Py'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip()) #remove os espacos inuteis
print(frase.rstrip())#remove espaco inutil a direita
print(frase.lstrip())#remove espcao inutil a esquerda
print(frase.split())#parte a frase nos locais de espaco
partido = frase.split()
print('-'.join(partido))#junta as palavras partidas usando um simbolo de escolha