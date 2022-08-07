'''DESAFIO 042 - Refaça o DESAFIO 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será
formado:
- Equilátero: Todos os lados são iguais.
- Isósceles: Dois lados iguais.
- Escaleno: Todos os lados são diferente.'''

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento : '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('PODE ser formado um triangulo com esses segmentos.')
    if (a == b == c):
        print('Tipo Equilátero')
        if a != b != c != a:
            print('Tipo escaleno')
    else:
        print('Tipo Isósceles')
else:
    print('NAO PODE ser formado um triangulo com esses segmentos.')
