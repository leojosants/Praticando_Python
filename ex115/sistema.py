'''Exercício Python 115a: Vamos criar um menu em Python, usando modularização.'''
'''Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.'''
'''Exercício Python 115c: Vamos finalizar o projeto de acesso a arquivos em Python.'''


from ex115.lib.interface import * # asterisco significa importar tudo
from ex115.lib.arquivo import * # asterisco significa importar tudo
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # opção de listar o conteúdo de um arquivo # deletado - cabeçalho('Opção 1') # print('Opção 1')
        lerArquivo(arq)

    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa - # cabeçalho('Opção 2') # print('opção 2')
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!') # print('Saindo do sistema... Até logo!')
        break

    else:
        print('\033[31mERRO. Digite uma opção válida!\033[m')
    sleep(2)

# FINAL DO VIDEO 115c

