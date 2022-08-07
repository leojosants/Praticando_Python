'''DESAFIO 019 -  Um professor quer sortear um dos seus quatro alunos para apagar o quandro. faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido'''

from random import choice
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
sort = choice(lista)
print('O aluno escolhido foi {}.'.format(sort))
