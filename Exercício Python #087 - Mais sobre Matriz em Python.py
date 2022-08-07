'''
Aprimore o desafio anterioe, mostrando no final: A) - A soma de todos os valores pares digitados; B) - A soma dos valores da terceira coluna; C) - O maior valor da segunda linha
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = cont = numpar = somatc = maiorsegl = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor na posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            numpar = matriz[l][c]
            soma += numpar
            cont += 1
#somatc = matriz[0][2] + matriz[1][2] + matriz[2][2]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma de todos os valores pares é {soma}.')
for l in range(0, 3):
    somatc += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somatc}.')
if matriz[1][0] and matriz[1][1] and matriz[1][2] == 0:
    maiorsegl = 0
else:
    if matriz[1][0] > maiorsegl:
        maiorsegl = matriz[1][0]
        if matriz[1][1] > maiorsegl:
            maiorsegl = matriz[1][1]
        if matriz[1][2] > maiorsegl:
            maiorsegl = matriz[1][2]
print(f'O maior valor da segunda linha é {maiorsegl}.')