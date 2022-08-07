'''Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.'''

'''VARIÁVEIS COMPOSTAS (DICIONARIOS)'''

'''RELEMBRANDO:
- TUPLAS: Declarada entre PARENTESES e os elementos separados por virgula. 
- LISTAS: Declarada entre COLCHETES e os elementos separados por virgula ou .
- DICIONÁRIOS: Declarada entre CHAVES e os elementos separados em virgula. '''

'''dados = dict()
dados = {'nome':'Pedro', 'idade':25}
dados['sexo'] = 'M'
print(dados)
print(dados['nome'])
print(dados['idade'])
print(dados['sexo'])
del dados['idade']
print(dados)'''

# FILME: É O ITEM, imprime todo conteudo
#TITULO, ANO, DIRETOR É A CHAVE
#STAR WARS, 1977 E GEROGE LUCAS É O ELEMENTO OU VALORES

'''filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'Goerge Lucas'}
print(filme)
print(filme['titulo'])
print(filme['ano'])
print(filme['diretor'])
print(filme.values())
print(filme.keys())
print(filme.items())

print('-='*20)

#IMPRESSÃO FORMATADA
for k, v in filme.items(): #para cada chave em valor (ITEM = TODO CONTEUDO)
    print(f'O {k} é {v}.')'''

'''pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':22}
#del pessoas['sexo']
pessoas['nome'] = 'Leandro'#SUBSTIUINDO GUSTAVO POR LEANDRO
pessoas['peso'] = 98.5 #ADICIONANDO PESO NO DICIONARIO PESSOAS
print(pessoas)
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos e é do sexo {pessoas["sexo"]}.')# PARA IMPRESSÃO DO ELEMENTO, TEM QUE SER ENTRE ASPAS DUPLAS, POIS JA ESTÁ DENTRO DE ASPAS SIMPLES
print(pessoas.keys()) #nome, sexo, idade
print(pessoas.values()) #elemntos da chave nome, sexo, idade
print(pessoas.items()) #todo conteudo do item pessoas

print('-='*30)
#IMPRESSÃO FORMATADA, ACESSANDO SOMENTE AS CHAVES
for k in pessoas.keys():
    print(k)

print('-='*30)
#IMPRESSÃO FORMATADA, ACESSANDO SOMENTE os valores
for v in pessoas.values():
    print(v)

print('-='*30)
#IMPRESSÃO FORMATADA, PARA ACESSAR O É NECESSÁRIO UTILIZAR AS CHAVES E O VALOR
for k, v in pessoas.items():
    #print(k, v)
    print(f'{k} = {v}')'''

#brasil = list()
'''brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
print(estado1)
print(estado2)
brasil.append(estado1) #ATENÇÃO, AGORA TUDO PASSA A SER INDICES
brasil.append(estado2) #ATENÇÃO, AGORA TUDO PASSA A SER INDICES
print(brasil)
print(len(brasil))
print(brasil[0])
print(brasil[0]['uf']) #imprimi o indice zero e o elemento uf
print(brasil[1])
print(brasil[1]['sigla'])'''


estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    print('-'*30)
    brasil.append(estado.copy())
print(brasil)
print('-='*20)

for e in brasil:
    print(e)
print('-='*20)

for e in brasil:
    for k, v in e.items():
        print(f'O {k} tem valor {v}')
print('-='*20)

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()