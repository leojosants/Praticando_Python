'''
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
'''pessoa = {}
galera = []
totid = somaid = mediaid = 0
mulheres = []
acimamedia = []
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if pessoa['sexo'] == 'F':
            mulheres.append(pessoa['nome'])
        if pessoa['sexo'] in 'MF':
            break
        print('\033[7mERRO! Por favor, digite apenas M ou F.\033[m')
    pessoa['idade'] = int(input('Idade: '))
    if pessoa['idade'] > mediaid:
        acimamedia = pessoa['nome']
    galera.append(pessoa.copy())
    totid += 1
    somaid += pessoa['idade']


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(galera)
print(f' - Foram cadastradas um total de {len(galera)} pessoas.')
mediaid = somaid / totid
print(f' - A média de idade das pessoas cadastradas é {mediaid:.2f} anos.')
print(f' - As mulheres cadastradas foram: {mulheres}')
print(galera)
print(f'As pessoas com idade acima da média é {acimamedia}')'''

galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('\033[7mERRO! Por favor, digite apenas M ou F\033[m')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('\033[7mERRO! Responda apenas S ou N\033[m')
    if resp == 'N':
        break
print('-=' * 30)
print(galera)
print(f'A) - Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) - A média de idade é de {media:5.2f} anos.')
print(f'C) - As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) - Lista das pessoas que estão acima da media: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')