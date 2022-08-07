'''AULA 17 - LISTAS'''

'''Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais'''

''' VARIÁVEIS COMPOSTAS (Listas) - Parte I '''

'''LISTAS SÃO ARMAZENADAS ENTRE COLCHETES E CADA ELEMENTO ENTRE ASPAS SIMPLES, SEPARADOS POR VIRGULA'''

'''lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
print(lanche)
print(len(lanche))
lanche[3] = 'Picolé' #Comando que permite substituir ou modificar um elemento
print(lanche)
print(len(lanche))
lanche.append('Coockie') #Comando para adicionar elemento, ele é adicionado automaticamente depois da ultima posição.
print(lanche)
print(len(lanche))
lanche.insert(0, 'Cachorro Quente')# Comando que insere um elemento na posição zero
print(lanche)
print(len(lanche))
#del lanche[3] #Comando que deleta o indice
print(lanche)
print(len(lanche))
print(lanche)
#lanche.pop(3) #Comando que deleta o indice
print(lanche)
lanche.pop() #Comando que elimina o ultimo indice
print(lanche)
print(len(lanche))
#lanche.remove('Pizza') #Comando que remove o conteudo
print(lanche)
print(len(lanche))
if 'Pizza' in lanche: #Comando que verifica se a Pizza esta dentro da lista, caso sim ela será remivida
    lanche.remove('Pizza')
else:
    print('O lanche pizza não foi encontrado.')
print(lanche)'''

'''valores = list(range(4, 11, 2)) #Comando que cria uma lista com os valores indicados por RANGE
print(valores)
print(len(valores))'''

'''valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)
print(len(valores))
valores.sort() #Comando que ordena em ordem alfabetica
print(valores)
print(len(valores))
valores.sort(reverse=True) #Comando que ordena em ordem reversa
print(valores)
print(len(valores))'''

'''num = [2, 5, 9, 1]
print()
num[2] = 3 #Comando que muta um indice, no caso no indice 2 substitua para 3
print(num)
num.append(7) #Comando que adiciona um elemento no final da lista
print(num)
num.sort() #Comando que ordena em ordem alfabetica ou numérica
print(num)
num.sort(reverse=True)#Comando que ordema em ordem reversa
print(num)
num.insert(2, 2) #Comando que substitui o elemento que estiver na posição 2 por 0.
print(f'Essa lista tem {len(num)} elementos.')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
#num.remove(2) #Comando que remove a primeira ocorrencia
if 4 in num:
    num.remove(4)
else:
    print('O valor 4 não foi encontrado')
#num.pop() #Comando que elimina o ultimo indice
print(num)
print(f'Essa lista tem {len(num)} elementos.')
#num.pop(2) #Comando que elimina a posição 2
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

'''valores = [] # Opção de Criação de lista vazia
valores = list() # Opção de Criação de lista vazia
print(valores)'''

#INSERINDO VALORES À LISTA VAZIA
'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)
#print(valores)
for v in valores: #Opção formatada de impressão
    print(f'{v}...', end='')

print('-'*10)
for c, v in enumerate(valores): #Opção de impressão com a posição do indice
    print(f'Na posição {c}, temos {v}.')
print('cheguei ao final da lista.')'''

#ACRESCENTANDO VALORES NA LISTA VAZIA A PARTIR DO TECLADO PELOR CONDIÇÃO FOR
'''valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista.')'''

'''a = [2, 3, 4, 7]
b = a #A tribui ao B a lista de A
b = a[:] #Atribui ao b a cópia de A
b[2] = 8 #B na posição 2, substitua para 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''