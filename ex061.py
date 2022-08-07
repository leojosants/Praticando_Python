'''DESAFIO 061 - Refaça o DESAFIO 051, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos
pa progrssão usando a estrutura while.'''
'''primeiroT = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiroT + (10 - 1) * razao
for c in range(primeiroT, decimo + razao, razao):
    print(c, end=' ->')
print('Acabou')'''

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
c = 1
while c <= 10:
    print(termo, end=' ')
    termo += razao
    c += 1
print('FIM')
