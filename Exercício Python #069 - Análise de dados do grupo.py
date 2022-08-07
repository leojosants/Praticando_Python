'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa devera perguntar se o usuario quer ou nao continuar. No final, mostre: A) - Quantas pessoas tem mais de 18 anos; B) - Quantos homens foram cadastrados; C) - Quantas mulheres tem menos de 20 anos.
'''
tot18 = toth = totm20 = 0
while True:
    print('CADASTRO DE PESSOA')
    print('=x=' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Ao todo, temos cadastrados {tot18} pessoas com mais de 18 anos.')
print(f'Ao todo, temos cadastrados {toth} homens.')
print(f'Ao todo, temos cadastrados {totm20} mulheres tem menos de 20 anos.')
