# leia o nome de uma cidade e diga se ela comeca com o nome 'SANTO'
print('Descobrir cidade:')

# city = str(input('Digite um nome de cidade:'))
# city_M = city.upper()
# city_split = city_M.split()
# santo = 'SANTO' in city_split[0]
#
#
# print(city_split)
# print('O nome da cidade digitado tem a palavra SANTO ? {}'.format(santo))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

city = str(input('Digite um nome de cidade:')).strip()
print(city[:5].upper() == 'SANTO')
