'''
CONDIÇÕES ANINHADAS(IF/ELIF/ELSE)
'''
nome = str(input('Qual seu nome? ')).strip()
if nome == 'Leonardo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Jéssica juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))