'''DESAFIO 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "F" ou "M". Caso esteja errado,peça a digitação novamente até ter um valor correto.'''

sexo = str(input('Digite seu sexo [M/F]: ')).upper()[0].strip()
while sexo not in 'MF': # Enquanto sexo nao for "MF"
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo "{}" registrado com sucesso!'.format(sexo))
