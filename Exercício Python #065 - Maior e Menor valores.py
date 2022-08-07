'''
Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar.
'''
resp = 'S'
cont = media = soma = menor = maior = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? ')).strip().upper()[0]
media = soma / cont
print('A média de todos os valores digitados é {:.2f}'.format(media))
print('O maior valor lido foi {} e o menor valor lido foi {}'.format(maior, menor))