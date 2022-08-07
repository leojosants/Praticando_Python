''''DESAFIO 062 - Melhore o DESAFIO 061, perguntando para o usuario
se ele quer mostrar mais alguns termos. O programa encerra quando
 ele disser que quer mostrar zero termos.'''

primeiro = int(input('Primeiro termo:'))
razao = int(input('A razao da PA: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} ->'.format(termo), end='')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
