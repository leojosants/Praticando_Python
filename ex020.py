'''DESAFIO 020 -  O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle
al1 = input('Nome primeiro aluno: ')
al2 = input('Nome segundo aluno: ')
al3 = input('Nome terceiro aluno: ')
al4 = input('Nome quarto aluno: ')
lista = [al1, al2, al3, al4]
shuffle(lista)
print('A órdem de apresentação será: {}'.format(lista))
