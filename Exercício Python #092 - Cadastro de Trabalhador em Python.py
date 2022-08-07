'''
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
CONSIDERAR APOSENTADORIA COM 35 ANOS DE CONTRIBUIÇÃO
'''
from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: ')).strip()
dados['idade'] = int(input('Ano de nascimento: '))
anoat = datetime.now().year
id = anoat - dados['idade']
dados['idade'] = id
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Sálario: R$ '))
    aposentadoria = id + (35 - (anoat - dados['contratação']))
    dados['aposentadoria'] = aposentadoria
    print('-=' * 30)
    print(dados)
    for k, v in dados.items():
        print(f'- {k} tem valor {v}.')

'''elif dados['ctps'] == 0:
    print('-=' * 30)
    print(dados)
    for k, v in dados.items():
        print(f' - {k} tem o valor {v}')'''