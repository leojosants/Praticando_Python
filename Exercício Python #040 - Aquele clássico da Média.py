'''Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a média atingida: - Média abaixo de 5.0 (REPROVADO); - Média entre 5.0 e 6.9 (RECUPERAÇÃO); - Média 7.0 ou superior (APROVADO)'''
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1 + n2) / 2
print('A média do aluno é: {}.'.format(media))
if media < 5:
    print('REPROVADO')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')