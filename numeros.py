
##import uteis # é recomendado importar toda biblioteca para que nao ocorra conflito de "ARQUIVOS"

#from uteis import fatorial, dobro, triplo

# As def(s), foram criadas em um outro arquivo (uteis.py), e será chamada como bibliotecas



from uteis import numeros # importação do pacote "NUMEROS" dentro do pacote "UTEIS"

# Programa Principal
num = int(input('Digite um valor: '))

fat = numeros.fatorial(num) # fat = uteis.fatorial(num)

#fat = fatorial(num)

print(f'O fatorial de {num} é: {fat}') # print(f'O fatorial de {num} é: {uteis.fatorial(num)}')

print(f'O dobro de {num} é : {numeros.dobro(num)}') # print(f'O dobro de {num} é: {uteis.dobro(num)}')

#print(f'O dobro de {num} é: {dobro(num)}')

print(f'O triplo de {num} é: {numeros.triplo(num)}') # print(f'O triplo de {num} é: {uteis.triplo(num)}')

#print(f'O triplo de {num} é: {triplo(num)}')