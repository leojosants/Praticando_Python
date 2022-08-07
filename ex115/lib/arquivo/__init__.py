from ex115.lib.interface import *

def arquivoExiste(nome):
    try: # tentar
        a = open(nome, 'rt') # open abrir o arquivo em modo texto - 'rt' significa: r para leitura - t para texto
        a.close() # fechar arquivo
    except FileNotFoundError: #se não der certo - se o arquivo não for encontrado
        return False
    else: # se der certo
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # open abrir o arquivo em modo texto - 'wt+' significa: escrever um arquivo de texto e o simbolo "mais" cria o arquivo caso nao exista.
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try: # tente
        a = open(nome, 'rt')
    except: # se der problema
        print('Erro ao ler o arquivo')
    else: # se nao der problema
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:# print(a.read()) # comando para ler tudo,  com quebra de linha
            dado = linha.split(';') # utilizando a funçao split para dividir entre ponto e virgula
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:.30} anos')
    finally: # finalizado
        a.close() # fechar arquivo


def cadastrar(arq, nome='desconhecido', idade=0):
    try: # tente
        a = open(arq, 'at') # abrir arquivo de texto - 'at': abrir texto
    except: # se der erro
        print('Houve um erro na abertura do arquivo!')
    else: # se nao der erro
        try: # tente (nesse caso tentar novamente se der erro)
            a.write(f'{nome};{idade}\n') # escrever dentro do arquivo
        except: # se nao der certo()
            print('Houve um ERRO na hora de escrever os dados! ')
        else: # se der certo
            print(f'Novo registro de {nome} adicionado.')
            a.close() # fechar arquivo

# FINAL DO VIDEO 115c