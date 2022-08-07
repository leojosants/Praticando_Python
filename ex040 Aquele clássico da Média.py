'''DESAFIO 040 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média:
- média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- MÉdia 7.0 ou superior: APROVADO'''

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1 + n2) / 2
print('A média entre {} e {} = {:.2f}'.format(n1, n2, media))
if media < 5.0:
    print('ALUNO REPROVADO')
elif media > 5.0 and media < 6.9:
    print('ALUNO EM RECUPERAÇÃO')
elif media == 7.0 or media > 7.0:
    print('ALUNO APROVADO')
