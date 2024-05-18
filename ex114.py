"""Crie um codigo em pytohn que testa  se o site do PUDIM esta acessivel pelo computador usado"""

import requests
try:
    url = requests.get('https://youtube.com')
except:
    print('erro')
else:
    print("O servidor está disponível.")
    print(url.apparent_encoding)

# import urllib
# import urllib.request
#
# try:
#     site = urllib.request.urlopen('https://pudim.com.br')
# except:
#     print('erro')
# else:
#     print('Deu certo')
