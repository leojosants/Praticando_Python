'''DESAFIO 053 - Crie um programa que leia uma frase qualquer e diga
se ela é um palindromo, desconsiderando os espaços.'''

frase = str(input(' Digite uma frase: ')).strip().upper()#elimina os espaços das extremidades/ transforma todas as letras em maiuscula
palavras = frase.split() # Geração de uma lista, separando cada palavra
junto = ''.join(palavras) #realiza a junção desconsiderando os espaços
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo.')
else:
    print('A frase digitada Não é um palindromo.')
