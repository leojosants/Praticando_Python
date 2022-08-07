'''
Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for inmpar, desconsidere-o
'''
s = cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('Foram informados {} numeros pares e a soma deles é {}'.format(cont, s))