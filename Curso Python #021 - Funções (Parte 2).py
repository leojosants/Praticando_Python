'''
Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python, o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python, escopo de variáveis e retorno de resultados.

FUNCOES PART 2

- INTERACTIVE HELP
- DOCSTRINGS
- ARGUMENTOS OPCIONIAIS
- ESCOPO DE VARIAVEIS
- RETORNO DE RESULTADOS
'''

'''
- INTERACTIVE HELP(AJUDA INTERATIVA)
- HELP()
'''

#help(print)

'''
print(input.__doc__)
help(input)
'''

'''- DOCSTRINGS'''
'''def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: sem retorno
    Funcão criada por Gustavo Guanabara do canal CursoemVideo
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


contador(2, 10, 2)
help(contador)'''

'''- PARAMETROS ADICIONAIS'''
'''def somar(a, b, c = 0):#iguala o parametro ou os parametros a zero
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar(a=3, b=9, c=4)'''

'''- ESCOPO DE VARIAVEIS'''
'''def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale{x} ')

#PROGRAMA PRINCIPAL
n = 2
print(f'No programa principal, n vale {n}')
teste()
#print(f'No programa principal, x vale {x}')#dara erro pois X tem escopo local'''

'''def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro, escopo local vale {a}')
    print(f'B dentro, escopo local vale {b}')
    print(f'C dentro, escopo local vale {c}')

#programa principal
a = 5
teste(a)
print(f'A fora, escopo global vale {a}')
#print(f'B fora, global vale {b}')#dara erro pois B tem escopo local
print('B fora escopo global, não funciona, pois tem escopo local')
#print(f'C fora, global vale {c}')#dara erro pois C tem escopo local
print('C fora escopo global, não funciona, pois tem escopo local')'''

'''def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro, escopo local vale {a}')
    print(f'B dentro, escopo local vale {b}')
    print(f'C dentro, escopo local vale {c}')

#programa principal
a = 5#perdera o valor 5 pois na DEF foi dado o comando global
teste(a)
print(f'A fora, escopo global vale {a}')
#print(f'B fora, global vale {b}')#dara erro pois B tem escopo local
print('B fora escopo global, não funciona, pois tem escopo local')
#print(f'C fora, global vale {c}')#dara erro pois C tem escopo local
print('C fora escopo global, não funciona, pois tem escopo local')'''

'''
- RETORNO DE VALORES (return)
'''
'''def somar(a=0, b=0, c=0):
    s = a + b + c
    #print(f'A soma vale {s}') - substitua o print por return s
    return s

#somar(3, 2, 5)#acrescenta à chamada somar em uma variavel
r1 = somar(3, 2, 5)
#somar(2, 2)#acrescenta à chamada somar em uma variavel
r2 = somar(2, 2)
#somar(6)#acrescenta à chamada somar em uma variavel
r3 = somar(6)
#realiza um print formatado
print(f'Os resultados foram {r1}, {r2} e {r3}')'''

#calculando o fatorial com a função return
'''def fatorial(num = 1):#caso o numero não receba valor ele valerá 1
    f = 1#variavel local
    for c in range(num, 0, -1):
        f *= c
    return f


#n = int(input('Digite um número: '))
#print(f'O fatorial de {n} é {fatorial(n)}')
#ou pode ser por variaveis recebendo a chamada fatorial
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')'''

#utilizando a função return retornando valor lógico
'''def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(f'O numero {num} é par? {par(num)}')
#print formatado com condição de controle
if par(num):
    print('É PAR!')
else:
    print('É IMPAR!')'''

#help(print)

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')