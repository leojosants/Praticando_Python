'''090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''
ficha = {}
ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input(f'Média de {ficha["nome"]}: '))
#print(ficha)
#print(f'Nome é igual a {ficha["nome"]}')
#print(f'Média é igual a {ficha["media"]}')
if ficha['media'] >= 7:
    ficha['situacao'] = 'Aprovado'
elif ficha['media'] < 7:
    ficha['situacao'] = 'recuperação'
else:
    ficha['situação'] = 'aprovado'
#print(ficha)

for k, v in ficha.items():
   print(f'{k} é igual a {v}')