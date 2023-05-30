import requests

try:
    requisicao = requests.get('https://r7.com/')
    print(requisicao.text)
except Exception as erro:
    print('Houve algum erro:', erro)
