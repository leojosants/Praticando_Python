'''DESAFIO 081: Crie um programa que vai ler vários números e colocar
em uma lista. Depois disso, mostre:
- Quantos numeros foram digitados.
- A lista de valores, ordenada de forma decrescente.
- Se o valor 5 foi digitado e está ou não na lista'''

val = []
while True:
    val.append(int(input('Digite um valor: ')))
    #resp = ' '
    resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'A lista criada foi: {val}')
print(f'Foram digitados {len(val)} valore(s).')
print(f'A lista criada e ordenada de forma crescente é: {sorted(val)}')
val.sort(reverse=True)
print(f'A lista criada e ordenada de forma decrescente é: {val}')
if val.count(5):
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi encontrado dentro da lista.')