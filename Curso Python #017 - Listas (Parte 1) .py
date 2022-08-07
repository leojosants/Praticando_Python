'''
Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

VARIAVEIS COMPOSTAS (LISTAS) PART I
    - Listas são representadas entre colchetes
    - Lista podem ser mutáveis
    - Lista pode-se adicionar elementos
    - Elementos em listas são chamados de chave ou key
'''

'''lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
print(lanche)
lanche[3] = 'Picole'#mutação de tupla, no indice 3 substitua por picole
print(lanche)'''

'''lanche.append('Cuck')#adicionameto automatico na ultima posição
print(lanche)
print('-=-' * 30)'''

'''lanche.insert(0, 'Cachorro Quente')#inserção de elemento em qualquer indice, nesse caso no indice zero, os indices são reorganizados automaticamente
print(lanche)'''
'''del lanche[3]#deletçaõ de indice, no caso indice 3
print(lanche)'''

'''#lanche.pop(3)#normalmente o metodo POP elimina o ultimo elemento, porem pode ser passado por parametro o indice que deseja eliminar, elimina pela chave/indice
print(lanche)
print('-=-' * 30)'''

'''lanche.pop()# sem passagem de parametro, elimina automaticamente o ultimo elemento, elimina pela chave/indice
print(lanche)
print('-=-' * 30)'''

'''lanche.remove('Pizza')#eliminar pelo elemento
print(lanche)
print('-=-' * 30)'''

'''lanche.pop()
print(lanche)
print('-=-' * 30)'''

#para eliminar elemento e verificar se este elemento consta na variável
'''if 'Pizza' in lanche:
    lanche.remove('Pizza')
print(lanche)
print('-=-' * 30)'''

'''valores = list(range(4, 11))
print(valores)
print('-=-' * 30)'''

#ordenando valores
'''valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)
valores.sort()#colocando em ordem crescente
print(valores)
valores.sort(reverse=True)#colocando em ordem decrescente ou inversa
print(valores)
print(len(valores))#quantidade de elementos
print('-=-' * 30)'''

'''num = (2, 5, 9, 1)
#num[2] = 3#retornara um erro, pois tuplas são imutáveis
print(num)
print('-=-' * 30)'''

'''num = [2, 5, 9, 1]
print(num)
num[2] = 3#mutação, substituiu o elemento que estava no indice 2 pelo valor 3
print(num)
print('-=-' * 30)

num.append(7)#adicionando o elemento 7, automaticamente ele se alocara no ultimo indice
print(num)
print('-=-' * 30)

num.sort()#ordenando elementos e não indices
print(num)
print('-=-' * 30)

num.sort(reverse=True)#ordenando de forma reversa
print(num)
print(f'Esta lista tem {len(num)} elementos.')
print('-=-' * 30)

#num.insert(2, 0)#insere o elemento no indice desejado, no caso inserir no indice 2 o elemento 0, os indices são organizados automaticamente
num.insert(2, 2)#insere o elemento no indice desejado, no caso insere no indice 2 o elemento 2, os indices são organizados automaticamente
print(num)
print('-=-' * 30)

#num.pop()#elimina o ultimo elemento e reorganiza os indices
'''#num.pop(2)#elimina o elemento da posição 2 e reorganiza os indices
#print(num)
#print('-=-' * 30)'''

#eliminando elementos
'''print(num)
num.remove(2)#elimina o elemento 2 na primeira ocorrencia
print(num)
print('-=-' * 30)'''

#para testar se um element consta na lista
'''if 4 in num:
    num.remove(4)#retornara um erro, pois o elemento 4 nao consta na lista
else:
        print('Não achei o numero 4')
print(num)
print('-=-' * 30)'''

'''num.remove(5)
print(num)
print('-=-' * 30)'''

'''valores = []#para se cria uma lista vazia, pode ser LIST () OU SOMENTE []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for v in valores:# para cada valor em valores...
    print(f'{v} ...', end='')
print()
print('-=-' * 30)'''

#impressão utilizando as chaves ou key
'''valores = []#para se cria uma lista vazia, pode ser LIST () OU SOMENTE []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for c, v in enumerate(valores):# para cada valor em valores...
    print(f'Na posição {c} encontrei o valor {v}.')'''

#ler valores pelo teclado é adicionar à lista e imprimir formatado mostrando o indice/posição
'''valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite o {cont}º valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')'''

'''a = [2, 3, 4, 7]
b = a
print(f'Lista A : {a}')
print(f'Lista B : {b}')'''

'''a = [2, 3, 4, 7]
b = a
b[2] = 8#realiza a mutação nas duas listas, devido à ligação de B = A
print(f'Lista A : {a}')
print(f'Lista B : {b}')'''

a = [2, 3, 4, 7]
b = a[:]#B recebendo à CÓPIA DE A, NESSE CASO REALIZA A MUTAÇÃO SOMENTE NA LISTA B
b[2] = 8#realiza a mutação SOMENTE na lista B devido estar recebendo a cópia de A, neste caso não há ligação de B e A
print(f'Lista A : {a}')
print(f'Lista B : {b}')