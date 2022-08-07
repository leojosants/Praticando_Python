'''DESAFIO 082: Crie um programa que vai ler vários números e
colocar em uma lista. Depois disso, crie duas listas extras que
 vão conter apenas os valores pares e os valores ímpares digitados,
 respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

val = []
par = []
imp = []
while True:
    n = int(input('Digite um valor: '))
    val.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        imp.append(n)
    if resp == 'N':
        break
print(f'A lista criada foi: {val}')
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores impares digitados foram: {imp}')

val = []
par = []
imp = []
while True:
    val.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(val):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        imp.append(v)
print('-='*30)
print(f'A lista criada foi: {val}')
print(f'A lista de pares é: {par}')
print(f'A lista de impares é: {imp}')