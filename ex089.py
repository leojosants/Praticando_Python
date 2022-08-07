'''DESAFIO 089: Crie um programa que leia nome e duas notas de vários
alunos e guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente.'''

'''temp = []
boletim = []
totmed = quant = 0

while True:
    nome = str(input('Nome: '))
    temp.append(nome)
    nota1 = float(input('Nota 1: '))
    temp.append(nota1)
    nota2 = float(input('Nota 2: '))
    temp.append(nota2)
    media = (nota1 + nota2) / 2
    #print(f'Média: {media}')
    quant += 1
    boletim.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break

    print('-='*30)
print(boletim)
print(f'A média do aluno {nome} é: {media}')
print(totmed / quant)'''

ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc =int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')