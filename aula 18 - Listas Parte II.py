'''Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
'''

'''VARIÁVEIS COMPOSTAS (LISTAS) - PARTE 2'''
'''Listas são declaradas dentro de colchetes e separados por virgula'''

'''dados = []
# OU
#dados = list()
dados.append('Pedro')
dados.append(25)
print(dados)
print(dados[0])
print(dados[1])
print('-='*20)
pessoas = []
pessoas.append(dados[:])#Adiciona a lista pessoas uma cópia da lista dados
print(pessoas)
print(pessoas[0][0])#Fatiamento, indece zero e elemento zero
print(pessoas[0][1])#Fatiamento, indice zero e elemento um'''

'''pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas)
print(len(pessoas))
print('-='*10)
print(pessoas[0]) #Imprimi todo conteudo da lista no indice zero
print(pessoas[0][0]) #Impirmi a lista no indice zero e o elemento 0
print(pessoas[0][1])
print('-='*10)
print(pessoas[1]) #Imprimi todo conteudo da lista no indice um
print(pessoas[1][0])
print(pessoas[1][1])
print('-='*10)
print(pessoas[2]) #Imprimi todo conteudo da lista no indice dois
print(pessoas[2][0])
print(pessoas[2][1])'''

'''teste = []
teste.append('Gustavo')
teste.append(40)
print(teste)
print(len(teste))
print(teste[0])
print(teste[1])

print('-='*10)

galera = []
print(galera)
galera.append(teste)
print(galera)
print(len(galera))'''

'''teste = []
teste.append('Gustavo')
teste.append(40)
print(teste)
print(len(teste))
print(teste[0])
print(teste[1])
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print(len(galera))'''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(len(galera))
print(galera[0])
print(galera[0][0])
print(galera[0][1])

print('-='*10)

print(galera[1])
print(len(galera[1]))
print(galera[1][0])
print(galera[1][1])

print('-='*10)

print(galera[2])
print(len(galera[2]))
print(galera[2][0])
print(galera[2][1])

print('-='*10)

print(galera[3])
print(len(galera[3]))
print(galera[3][0])
print(galera[3][1])

print('-='*10)

#IMPRESSÃO FORMATADA DE TODO INDICE
for p in galera:
    print(p)

print('-='*10)

#IMPRESSÃO FORMATADA DA POSIÇÃO ZERO DO INDICE
for p in galera:
    print(f'Nome: {p[0]}')

print('-='*10)

#IMPRESSÃO FORMATADA DA POSIÇÃO UM DO INDICE
for p in galera:
    print(f'Idade: {p[1]}')

print('-='*10)

#IMPRESSÃO FORMATADA DO INDICE COM CADA POSIÇÃO
for p in galera:
    print(f'Nome: {p[0]} tem Idade: {p[1]} anos.')'''

#VERIFICANDO MAIOR E MENOR
'''galera = []
dados = []
totmai = totmen = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'temos {totmai} maiores e {totmen} menores de idade.')'''