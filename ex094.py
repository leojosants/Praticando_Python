'''094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

'''dados = dict() # OU dados = {}
pessoas = list() # OU pessoas = []
totid = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    dados['idade'] = int(input('Idade: '))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    pessoas.append(dados)
    totid += dados['idade']
    if resp == 'N':
        break
print('-='*30)
#print(pessoas)
print(f'- O grupo tem {len(pessoas)} pessoa(s).')
media = totid / len(pessoas)
print(f'- A média de idade é de {media} anos.')
print(pessoas)
dados['mulheres'] = dados['sexo']
pessoas.append(dados)
if dados['sexo'] == 'F':
    print(f'- As mulheres cadastradas foram : {dados["nome"]}')

print(dados)
#if pessoas['sexo']:
#    print('femini')'''

pessoa = dict() # OU pessoa = {}
galera = list() # OU galera = []
totid = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('\033[7mERRO! Por favor, digite apenas M ou F.\033[m')
    pessoa['idade'] = int(input('Idade: '))
    totid += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('\033[7mERRO! Por favor digite apenas S ou N.\033[m')
    if resp == 'N':
        break
print('-='*30)
print(f'A) - Ao todo temos {len(galera)} pessoas cadastradas.')
media = totid / len(galera)
print(f'B) - A média de idade é {media:5.2f} anos.')
print(f'C) - A mulheres cadastradas foram ', end=' ')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
print()
print(f'D) - Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print(' <<< ENCERRADO >>> ')