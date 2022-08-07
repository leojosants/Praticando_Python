'''Condições Simples e Compostas
- Condição simples = somente if
- Condição composta = if e else
'''
'''nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo voce tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'. format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABENS')
else:
    print('Sua media foi ruim! ESTUDE MAIS')