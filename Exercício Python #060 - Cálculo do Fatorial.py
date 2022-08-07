'''
Faca um programa que leia um numero qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
from math import factorial# importacão da biblioteca MATH somente o metodo FACTORIAL
num = int(input('Digite um número para \ncalcular seu Fatorial: '))# solicitando valor
print('O Fatorial de {} é {}.'.format(num, factorial(num)))# print a varial NUM  e o resultado do metodo FACTORIAL DE NUM

print('-+-' * 20)# informação

n = int(input('Digite um número para \ncalcular seu Fatorial: '))# solicitando um valor
c = n# variável C recebendo o INPUT de N
f = 1# varável F recebendo o valor
print('Calculando {}! = '.format(n), end='')# print informação sem quebra de linha
while c > 0:# enquanto o INPUT de C for MAIOR que zero
    print('{}'.format(c), end='')# print do INPUT de C sem quebra de linha
    print(' x ' if c > 1 else ' = ', end='')# print com estrutura composta simplificada, imprima X se o INPUT de C for maior que 1, SENAO imprimi =, sem quebra de linha
    f *= c# variável F recebendo ela mesmo (1) acrescentando o INPPUT de C
    c -= 1# variavel C recebendo ela mesmo (IMPUT de c), subtraindo 1
print('{}'.format(f))# print do resultado da variavel F