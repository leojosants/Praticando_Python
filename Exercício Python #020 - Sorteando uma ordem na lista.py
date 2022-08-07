'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faca um programa que leia o nme dos quatro aunos e mostre a ordem sorteada.'''
import random
al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno:'))
al4 = str(input('Quarto aluno: '))
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print('A ordem de apresentção será {}'.format(lista))