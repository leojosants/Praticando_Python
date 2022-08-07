'''092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
anonsc = int(input('Ano de nascimento: '))
#anoatualcomp = datetime.now().year
anoatual = 2018
#print(anoatualcomp)
id = (2018 - anonsc)
#id = (anoatual - anonsc)
cadastro['idade'] = id
cadastro['CTPS'] = int(input('CTPS (0 não tem): '))
#print(cadastro)
if cadastro['CTPS'] != 0:
    cadastro['Ano Contratacao'] = int(input('Ano de contratação: '))
    aposentar = (cadastro['Ano Contratacao']) + cadastro['idade'] + 35 - 2018#datetime.now().year
    cadastro['salario'] = float(input('Salário: R$'))
    cadastro['aposentar'] = aposentar
else:
    print('Sem carteira de trabalho')
print('-='*30)
for k, v in cadastro.items():
    print(f'- {k} tem o valor: {v}')
