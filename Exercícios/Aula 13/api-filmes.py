#Não está funcionando

import requests
import json

def requisicao(titulo):
    try:
        permissao = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=2f32baa0')
        req = requests.get('http://www.omdbapi.com/?t=' + titulo)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexão')
        return None

def printar_detalhes(filme):
    print('Título:', filme['Title'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Nota:', filme['imdbRating'])
    print('')


sair = False
while not sair:
    op = input('Escreva o nome de um filme em inglês ou SAIR para fechar: ')

    if op == 'sair' or op == 'Sair':
        op = 'SAIR'
    
    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'True':
            printar_detalhes(filme)
        else:
            print('Filme não encontrado')
