'''Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python, o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python, escopo de variáveis e retorno de resultados.'''

'''FUNÇÕES PARTE II'''

# Interactive Help

# Docstrings

# Argumentos opcionais

# Escopo de variáveis
    # Escopo Global
    # Escopo Local
    # Variável Global
    # Variável Local

# Retorno de resultados

'''--------------------------------------------------------------------------------------------------'''
# INTERACTIVE HELP
'''help(print) # OU
print('-'*30)
print(input.__doc__)
#help(len)
#help(int)
#help(float)'''


# DOCSTRINGS
'''def contador(i,f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagm
    :param f: fim da contagem
    :param p: paso da contagem
    :return: sem retono
    Função criada por Gustavo guanabara do canal CursoEmVídeo
    """
    c = i
    while c <= f:
        print(f'{c}', end='.. ')
        c += p
    print('FIM!')

contador(2, 10, 2)
help(contador)'''


# PARÂMETROS OPCIONAIS
'''
"""def somar(a=0, b=0, c=0): # Paramentros opcionais a = 0, b = 0, c = 0
    ->Realiza a soma de a + b+ c
    :param a: Recebe o primeiro valor
    :param b: Recebe o segundo valor
    :param c: Recebe o terceiro valor
    :return: sem retorno
    """
    s = a +b +c
    print(f'A soma vale {s}')


somar(3, 3)
somar(b = 3, c = 2)
somar(c = 3, a =2)
somar()
'''

'''------------------------------------------------------------------------------------------------------------------'''

# ESCOPO DE VARIAVEIS
#
'''def teste():
    print(f'Na Função teste, "N" vale {n}.')


# Programa Principal
n = 2
print(f'No Programa Principal, "N" vale {n}.')
teste()'''


#
'''def teste():
    x = 8 # Variavel local
    print(f'Na função teste, "N" vale {n}.')
    print(f'Na Função teste, "X" vale {x}.')

# Programa Principal
n = 2 #Variavel Global
print(f'No Programa Principal, "N" vale {n}')
teste()
#print(f'No Programa Principal, "X" vale {x}.') # Informará umerro, pois "X" foi declarada dentro da função, daí ela é uma variavel local.'''


#
'''def teste(b):
    b += 4 # Vai receber o valro de A passado pelo parabetro B e somarará com 4.
    c = 2 # Variavel local
    print(f'Na Funcão teste, "A" vale {a}. ')
    print(f'Na Função teste, "B", vale {b}.')
    print(f'Na Função teste, "C" vale {c}.')


# Programa Principal
a = 5 #Variavel global
teste(a)
print(f'"A" no Programa Principal vale {a}.')
#print(f'"B" no Programa Principal vale {b}.') # Dará erro, pois a variavel "B" e´somento local
#print(f'"C" no Programa Princopal vale {c}.') # Dará erro, pois a variavel "C" e´somento local'''


#
'''def teste(b):
    a = 8 # Variavel local
    b += 4 # Vai receber o valro de A passado pelo parabetro B e somarará com 4.
    c = 2 # Variavel local
    print(f'Na Funcão "teste", "A" vale {a}. ')
    print(f'Na Função "teste", "B", vale {b}.')
    print(f'Na Função "teste", "C" vale {c}.')

# Programa Principal
a = 5 #Variavel global
teste(a)
print(f'"A" no Programa Principal vale {a}.')
#print(f'"B" no Programa Principal vale {b}.') # Dará erro, pois a variavel "B" e´somento local
#print(f'"C" no Programa Princopal vale {c}.') # Dará erro, pois a variavel "C" e´somento local'''


#
'''def função():
    n1 = 4
    print(f'Na Função "função", "n1" vale {n1}.')

# Programa Principal
n1 = 2
função()
print(f'No Programa Principal, "n1" vale {n1}.')'''


# Tratando Variavel global
#
'''def test(b):
    global a # Função que ordena transformar a variavel "A" como global, sendo o valor 8 tambem no Programa Principal
    a = 8
    b += 4
    c = 2
    print(f'Na Função "teste", "A" vale {a}.')
    print(f'Na Função "teste", "B" vale {b}.')
    print(f'Na Função "teste", "C" vale {c}.')

# Programa Princippal
a = 5
test(a)
print(f'No Programa Principal, "A" vale {a}.')
#print(f'No Programa Principal, "B", vale {b}.') # ERRO, FUNCIONA SOMENTE DENTRO DO ESCOPO LOCAL
#print(f'No Programa Principal, "C", vale {c}.') # ERRO, FUNCIONA SOMENTE DENTRO DO ESCOPO LOCAL'''


# RETORNO DE VALORES (return)
#
'''def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s # retira o print e substitui pelo retorn - print(f'A soma vale {s}.')

# Programa Principal
resp = somar(3, 2, 5) # o retorn será encaminhado pra variavel RESP ou somente print
print(f'A soma vale {somar(3, 2, 5)}.')
print(f'A soma vale {resp}.')
r1 = somar(2, 2)
print(somar(2, 2))
print(f'A soma vale {r1}.')
r2 = somar(6)
print(somar(6))
print(f'A soma vale {r2}.')
r3 = somar(8)
print(somar(8))
print(f'A soma vale {r3}.')
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')'''


#
'''def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s

# Programa Principal
r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3}.')'''


#
'''def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

# Programa Principal
n = int(input('Digite um número: '))
#print(fatorial(n)) # OU
print(f'O fatorial de {n} é igual a {fatorial(n)}.')
r1 = fatorial(5)
r2 = fatorial(4)
r3 = fatorial()
print(f'Os resultados são: {r1}, {r2} e {r3}.')'''


# Retornando valor logico
#
'''def Par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False

# Programa Principal
num = int(input('Digite um valor: '))
if Par(num):
    print(f'O valor {num} é par!.')
else:
    print(f'O valor {num} é ímpar.')'''