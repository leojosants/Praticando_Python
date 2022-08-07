'''
Crie um programa que tenha uma tupla com varias palavras (não usar acentos). Depois disso, voce deve mostrar, para cada palavra, quais são as vogais
'''
lista = ('programacao', 'tecnologia', 'gerenciamento', 'armazenamento',
         'dispositivo', 'funcoes', 'metodos', 'caracteres', 'iteracao',
         'python', 'algoritmo')
for p in lista:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')