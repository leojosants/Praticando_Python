'''
Faca um programa que leia o nome e a media de um aluno, guardando tambem a situação em um dicionário. No final, mostre o conteudo da estrutura na tela.
'''

aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'A media de {aluno["nome"]}: '))
print('-=' * 30)
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] >= 5 and aluno['media'] < 7:
#OU elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
#print(aluno)
for k, v in aluno.items():
    print(f'{k} é {v}')