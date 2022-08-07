''' DESAFIO 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
totpar = somac3 = maior = 0
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, [{c}]:  '))
print(matriz)
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            totpar += matriz[l][c]
    #somac3 = (matriz[0][2]) + (matriz[1][2]) + (matriz[2][2])
    print()
print('-='*30)
print(f'A soma dos valores pares é: {totpar}')

#OUTRA OPÇÃO DE BUSCA DAS COLUNAS
for l in range(0,3):
    somac3 += matriz[l][2]
print(f'A soma dos valores da teceira coluna é: {somac3}')

#verificando qual é o maior valor da segunda linha
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda coluna é: {maior}')
