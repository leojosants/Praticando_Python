'''Exercício Python 114: Crie um código em Python que teste se o
site pudim está acessível pelo computador usado.'''

import urllib
import urllib.request

try: # Tente
    site = urllib.request.urlopen('http://www.pudim.com.br')

#except Exception as erro:
#    print(erro) # erro que apresenta com a internet desativada: <urlopen error [Errno 11001] getaddrinfo failed>

except urllib.error.URLError: #except: # se der falha
    print('O site "PUDIM" não está acessivel no momento.') #print('Não deu certo') # tem que desativar internet e rodar o programa

else: # Se não der falha
    print('Consegui acessar o site "PUDIM" com sucesso.') #print('Deu certo') # a internet tem que estar conectada

finally:
    print('Programa Finalizado ! ! !')

# adicional
#print(site.read()) # Informa o código fonte do site