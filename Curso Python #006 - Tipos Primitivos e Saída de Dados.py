'''TIPOS PRIMITIVOS:
INT, FLOAT, BOOL, STR'''

'''n1 = int(input('Digite um numero: '))
n2 = int(input('Digite mais um numero: '))
s = n1 + n2
#print('A soma vale', s)
print('A soma vale {}'. format(s))
#print('A soma entre', n1, 'e', n2, 'é', s)
print('A soma entre {} e {} é {}'.format(n1, n2, s))'''

n1 = input('Digite algo: ')
#realiza a verificação somente com o tipo primitivi não especificado
print(n1.isnumeric())#é número?
print(n1.isalpha())# é letra?
print(n1.isalnum())# é alfanumérico?
print(n1.isupper())# está em letras maiusculas?
print(n1.islower())# está em minuscula?
