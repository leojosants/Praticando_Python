'''DESAFIO 065 -  Crie um programamnque leia varios numeros inteiros
pelo teclado. No final da execução, mostre a media entre todos os valores
e qual foi o maior e o menor valores lidos. O programa deve perguntar ao
usuario se ele quer ou nao continuar a digitar os valores'''

resp = 'S'
totmed = media = cont = maior = menor = 0
while resp not in 'N':
    n = int(input('Digite um número: '))
    totmed += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
media = totmed / cont
print('A media entre os {} valores digitados é: {:.2f}.'.format(cont, media))
print('O maior valor é {} e o menor é {}.'.format(maior, menor))
