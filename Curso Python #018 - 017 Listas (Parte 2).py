'''
VARIÁVEIS COMPOSTAS - LISTAS PARTE II
- Lista é mutavel

'''

'''dados  = []
dados.append('Pedro')
dados.append(25)
print(dados)
print(dados[0])
print(dados[1])

print('-=-' * 20)

pessoas = []
pessoas.append(dados[:])#adiciona uma cópia de uma lista dentro de outra lista
print(pessoas)'''

'''pessoas = []
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas)
print(pessoas[0][0])#analisa e imprimir o indice ZERO e o elemento ZERO dentro do indice ZER
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])#analise e imprimi todU o conteudo do indice UM'''

'''teste = []
teste.append('Gustavo')
teste.append(40)
print(teste)'''

'''teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste)
print(f'Lista TESTE = {teste}.')
print(f'Lista GALERA = {galera}')'''

'''teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
#print(f'Lista TESTE = {teste}.')
print(f'Lista GALERA = {galera}')'''

#estrutura com ligação
'''teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
#galera.append(teste)
galera.append(teste[:])#copia
teste[0] = 'Maria'
teste[1] = 22
#galera.append(teste)
galera.append(teste[:])#copia
#print(f'Lista TESTE = {teste}.')
print(f'Lista GALERA = {galera}')'''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(f'A lista GALERA possui {len(galera)} indices')
print(f'Conteudo do indice 0 = {galera[0]}')
print(f'Indice 0, elemento 0 = {galera[0][0]}')
print(f'Indice 0, elemento 1 = {galera[0][1]}')
print('-' * 20)
print(f'Conteudo do indice 1 = {galera[1]}')
print(f'Indice 1, elemento 0 = {galera[1][0]}')
print(f'Indice 1, elemento 1 = {galera[1][1]}')
print('-' * 20)
print(f'Conteudo do indice 2 = {galera[2]}')
print(f'Indice 2, elemento 0 = {galera[2][0]}')
print(f'Indice 2, elemento 1 = {galera[2][1]}')
print('-' * 20)
print(f'Conteudo do indice 3 = {galera[3]}')
print(f'Indice 3, elemento 0 = {galera[3][0]}')
print(f'Indice 3, elemento 1 = {galera[3][1]}')'''

'''
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera)
for indice in galera:
    print(indice)

#imprimindo somente os NOMES (elemento 0)
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera)
for indice in galera:
    print(f'Nome = {indice[0]}')

#imprimindo somente as IDADES (elemento 1)
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera)
for indice in galera:
    print(f'Idade = {indice[1]}')

#imprimindo NOME E IDADES (elemento 0 e 1)
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera)
for indice in galera:
    print(f'{indice[0]} tem {indice[1]} anos de idade.')
'''
'''
galera = []
dado = []
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()#elimina o conteudo da lista
#print(dado)
print(galera)
'''

#Análisando idade e impressão formatada
galera = []
dado = []
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()#elimina o conteudo da lista cada vez que faz o laço
#print(dado)
print(galera)
for indice in galera:
    if indice[1] >= 21:
        print(f'{indice[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{indice[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')