'''MANIPULANDO CADEIAS DE TEXTO'''

#FATIAMENTO DE STRING (busca pedaços)
frase = 'Curso em Video Python'
print('A variável FRASE recebe a string = ', frase)

print('A letra no indice 9 é: ', frase[9])#busca a letra no indice 9 da string

print('As letras do indice 9 ao indice 12 é: ', frase[9:13])#busca do indice 9 ate um indice a menos que 13, no caso ate 12

print('As letras do indice 9 ao indice 20 é: ', frase[9:21])# busca do indice 9 ate um indce a menos que 21, no caso ate 20

print('As letras do indice 9 ao indice 20 pulando de 2 em dois é: ', frase[9:21:2])#busca do incice 9 ate um indice a menos que 21, no caso ate 20 pulando de 2 em 2

print('As letras do indice 0 ao indice 4 é: ', frase[:5])#busca do primeiro indice ate um indice a menos que 5, no caso ate 4

print('As letras do indice 15 até o ultimo indice é: ', frase[15:])#busca do indice 15 ate o final, no caso ate 20

print('As letras do indice 9 ate o ultimo indice pulando de 3 em 3 é: ', frase[9::3])#busca do indice 9 ate o ultimo indice, no caso 20, pulando de 3 em 3

#ANALISE DE STRING
print('O comprimeto da string é: ', len(frase), 'indices')#busca o comprimento da string

print('A letra "O" maiuscula, aparece ', frase.count('O'), 'veze(s)')#busca quantas vezes existe a letra "O" maiuscula dentro da string

print('A letra "o" minuscula, aparece', frase.count('o'), 'veze(s)')#busca quantas vezes existe a letra "o" minusculo dentro da string

print('O "o" minusculo do indice 0 ao indice 12, aparece ', frase.count('o', 0, 13), 'veze(s)')#realiza o fatiamento e a contagem

print('Os caracteres "deo" minuscula, foi encontrado inciando no indice', frase.find('deo'))#busca em que momento começou, em que indice começou os caracteres dentro da string, caso não apareca retorna o valor -1

print('Os caracteres "Androide" capitalizado, foi encontrado iniciando no indice', frase.find('Androide'))#busca em que momento começou, em que indice começou os caracteres dentro da string, caso não apareca retorna o valor -1

print('Existe os caracteres "Curso", dentro da frase?', 'Curso' in frase)#busca se exite o caracter dentro da frase, retorna SIM/TRUE ou NÃO/FALSE

#TRANSFORMAÇÃO DE STRING - OBS: PODE SER TRANSFORMADO E NÃO MUTÁVEL
print(frase)

print('Dentro da frase -', frase,'- , substitua a palavra "Python em "Android"- ', frase.replace('Python', 'Android'))#substitui a palavra em outra de forma secundaria, porém não salva

print('Transforma de forma secundária os caracteres da frase em maiuscula - ', frase, '-', frase.upper())#transforma os caracteres em maiusculo, permanecendo os que já se encontram

print('Transforma de forma secundária os caracteres da frase em minuscula - ', frase, '-', frase.lower())#transforma os caracteres em minusculo, permanecendo os que já se encontram

print('Transforma de forma secundária os caracteres da frase em minuscula, e somente mantem o indice zero em maiuscula',frase, '-',frase.capitalize())#transforma todas os caracteres em letras minusculas e transforma somento o primeiro indice para maiuscula

print('Transforma o primeiro caracter de cada palavra em maiuscula - ', frase, '-', frase.title())#onde possue espaço, esta função realiza a quebra e transforma o primeiro indce de cada palavra em maiuscula

print('Remove os espaços somente das extremidades', '(', frase,')', '-', '(', frase.strip(),')')#remove os espaços somente das extremidades

print('Remove somente os ultimos espaços', '(', frase,')', '-', '(',frase.rstrip(),')')#remove somente os espaços da direita, mantendo os da esquerda

print('Remove somente os ultimos espaços', '(', frase,')', '-', '(',frase.lstrip(),')')#remove somente os espaços da esquer, mantendo os da direita

#DIVISÃO DE STRINGS
print('Gerando lista = ', frase.split())#Ocorre um divisão entre os espaços, gerando uma lista

#JUNÇÃO DE STRING
print('-'.join(frase))
print()
print("""Parabéns! Que o seu dia seja tão lindo quanto o seu sorriso e lhe ofereça tanta felicidade quanto a sua amizade envia para a minha vida. Que esta nova etapa chegue recheada de muita saúde e novas oportunidades para concretizar os seus sonhos mais desejados.
Que a alegria acompanhe você por todos os momentos e que Deus continue guiando todos os seus passos e iluminando cada vez mais os seus pensamentos. 
Faça com que a sua simpatia possa contagiar ainda mais pessoas, pois você é uma pessoa de muito brilho e a humanidade merece que sua luz seja compartilhada.
Nunca se esqueça quanto é especial para a minha vida e de tantas outras pessoas. Feliz""")