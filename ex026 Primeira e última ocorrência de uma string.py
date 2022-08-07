''' DESAFIO 026 - Primeira e última ocorrência de uma string - Faça um programa que leia a frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição a letra "A" aparece a primeira vez.
- Em que posição a letra "A" aparece a ultima vez'''

frase = str(input('Digite uma frase: ')).strip().upper()
print(frase)
print('Quantas vezes aparece a letra "A": {}'.format(frase.count('A')))
print('A primeira letra "A", aparece na posição: {}'.format(frase.find("A")))
print('A ultima letra "A", aparece na posição  : {}'.format(frase.rfind("A")))
