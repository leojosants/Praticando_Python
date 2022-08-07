''' MANIPULANDO TEXTO'''

# FATIAMENTO
#----------------------------
'''frase = 'Curso em Video Python'
print('Na variável = {}, O índice [9] contém o caracter: {}'.format(frase, frase[9]))
print('Na variável = {}, entre os índices [9:13], correspondem a: {}'.format(frase, frase[9:13])) #não conta o ultimo índice
print('Na variável = {}, entre os indices [9:21], correspondem a: {}'.format(frase, frase[9:21])) #não conta o ultimo índice
print('Na variável = {}, entre os indices [9:21:2], pulando de dois em dois, correpondem a: {}'.format(frase, frase[9:21:2]))
print('Na variável = {}, entre os indices [:5], corresponde a: {}'.format(frase, frase[:5])) #Quando se inicia somente com dois pontos, a verificação se iniciará no indice zero
print('Navariável {}, entre os indices [15:], corresponde a: {}'.format(frase, frase[15:])) #Quando finaliza com dois pontos, a verificação irá ate o final
print('Na variavel {}, os indices [9::3], corresponde a: {}'.format(frase, frase[9::3])) # Comeca no nove, vai até o final pulando de 3 em 3.
'''


# ANÁLISE
#----------------------------
'''frase = 'Curso em Video Python'
print(len(frase)) # comprimento da frase, quantidades de caracteres
print(frase.count('o')) # Verifica o total de letras 'o' minusculos
print(frase.count('o', 0, 13)) # verifica o total de 'o' minusculo de 0 a 13
print(frase.find('deo')) # Em que posição começou os caracteres 'deo'
print(frase.find('Android')) # Verifica se existe, caso não retorna -1
print('Curso'in frase)# Verifica se palavra 'Curso' dentro da frase, retornará True (verdadeiro) ou False (Falso)
'''


# TRANSFORMAÇÃO
#----------------------------
'''frase = 'Curso em Video Python'
print(frase)
print(frase.replace('Python', 'Android')) # substitui 'Python' por 'Android'
print(frase.upper()) # Transforma todos os caracteres em maiúscula, mantendo as que já estiverem em maiuscula
print(frase.lower()) # Transforma todos os caracteres em minusculo, mantendo as que ja estiverem em minuscula
print(frase.capitalize()) # Transforma todos os caracteres em minusculo e transfoma somente o primeiro caracter em maiuscula
print(frase.title()) # Transforma o primeiro caracater de cada palavra em maiuscula'''

'''frase ='  Aprenda Python   '
print(frase)
print(len(frase))
print(frase.strip()) # Elimina os espaços nas extremidades
print(len(frase.strip()))
print(frase.rstrip()) # Remove somente os ultimos espaços ou da direita
print(len(frase.rstrip()))
print(frase.lstrip()) # Remove somente os primeiros espaços ou da esquerda
print(len(frase.lstrip()))'''


# DIVISÃO
#______________________________
'''frase = 'Curso em Video Python'
print(frase)
print(len(frase))
print(frase.split()) # Onde houver espaço, haverá uma divisão, indexcando cada letra  de cada palavra, ou seja, transformnando cada letra de uma palavra em indice.'''


# JUNÇÃO
#----------------------------
'''frase = 'Curso em Video Python'
print(frase)
print('-'.join(frase)) # junta cada palavra e realiza a separação por '-' '''

