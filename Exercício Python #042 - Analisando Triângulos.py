'''Refaca o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado: - EQUILÁTERO: Todos os lados iguais; - ISOSCELES: Dois lados iguais; - ESCALENO: Todos os lados diferentes'''
a = float(input('Segmento A: '))
b = float(input('Segmento B: '))
c = float(input('Segmento C: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triangulo ', end='')
    if a == b == c:
        print('EQUILATERO')
    elif a != b != c != a:
            print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo.')