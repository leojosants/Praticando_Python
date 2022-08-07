'''DESAFIO 077: Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais.'''

listagem = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for p in listagem:
    print(f'\nNa palavra {p} temos:', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
