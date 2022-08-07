'''
Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

ESTRUTURAS COMPOSTAS - DICIONÁRIOS

TUPLAS, LISTAS E DICIONARIOS
  ()      []        {}

- Dicionarios são estruturas de dados semelhantes às tuplas e as listas, porem com possibilidade de personalização dos indices.
- Dicionário não permite cria cópia assim [:], usa-se o metodo ponto copy
- Dicionários permite acessar itens(items), chaves(keys) ou os valores(values)
    - ÍIENS(items): Valores e Chaves
    - CHAVES(keys): Indice
    - VALORES (values): Dados do indice

- REPRESENTAÇÃO: EXEMPLO = dict() OU EXEMPLO = {'nome':'Pedro', 'Idade':25}
'''

'''
dados = {'nome': 'Pedro', 'Idade': 25}#INDICE nome, INDICE idade
print(dados)
print(dados['nome'])
print(dados['Idade'])
dados['sexo'] = 'M'#incluindo dados
print(dados)
print(dados['sexo'])
del dados['Idade']#elimina o INDICE idade
print(dados)
'''

'''
filme = {'Título': 'Star Wars',
         'Ano': 1977,
         'Diretor': 'George Lucas'}
print(filme)
for k, v in filme.items():#para cada chave e valor no filme ponto itens (realiza a busca dos itens chave e valor)
    print(f'O {k} é {v}.')
    '''

'''
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(f'A quantidade de INDICES ou CHAVES é: {len(pessoas)}')
#print(pessoas[0])
print(f'Os ITENS são: {pessoas.items()}')
print(f'Os INDICES OU CHAVES são: {pessoas.keys()}')
print(f'Os DADOS ou VALORES dos INDICES ou CHAVES são: {pessoas.values()}')

print('-' * 20)
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
for k, v in pessoas.items():#para cada chave e valor no filme ponto itens (realiza a busca dos itens chave e valor)
    print(f'O {k} é {v}.')
'''

#CRIANDO DICIONARIO DENTRO DE UMA LISTA
'''
brasil = []# declaração de uma LISTA vazia
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)#adiciona o DICIONÁRIO estado1 dentro da LISTA brasil
brasil.append(estado2)#adiciona o DICIONÁRIO estado2 dentro da LISTA brasi2
print(estado1)#iprimi o DICIONARIO estado1
print(estado2)#imprimi o DICIONARIO estado2
print(brasil)#imprimi a LISTA brasil contendo o input dos DICIONARIOS estado1 e estado2.
print('-----')
print(brasil)
print(f'brasil no indice ZERO = {brasil[0]}')# imprimi a LISTA brasil no infice ZERO
print(f'brasil no indice ZERO, VALOR uf = {brasil[0]["uf"]}')
print(f'brasil no indice ZERO, VALOR sigla = {brasil[0]["sigla"]}')

print('-----')
print(f'brasil no indice UM = {brasil[1]}')# imprimi a LISTA brasil no infice UM
print(f'brasil no indice UM, VALOR uf = {brasil[1]["uf"]}')
print(f'brasil no indice UM, VALOR sigla = {brasil[1]["sigla"]}')
'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).strip()
    estado['sigla'] = str(input('Sigla do Estado: ')).strip()
    brasil.append(estado.copy())
print(brasil)

print('-----')

#impressão formatada
#for para a LISTA brasil
for e in brasil:
    print(e)

print('-----')

#impressão formatada
#for para a LISTA brasil e um for para o DICIONARIO ESTADO
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

print('-----')

#impressão formatada
#for para a LISTA brasil e um for para o DICIONARIO ESTADO
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()