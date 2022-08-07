'''
Faca um programa que leia o sexo de uma pessoa, mas so aceita os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente ate ter um valor correto.
'''
'''sexo = ''
while sexo != 'MmFf':
    sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()
    if sexo == 'M' or sexo == 'm' or sexo == 'F' or sexo == 'f':
        print('Sexo {} registrado com sucesso.'.format(sexo))
    else:
        print('Dados inválidos. Por favor, informe seu sexo: ')'''

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))