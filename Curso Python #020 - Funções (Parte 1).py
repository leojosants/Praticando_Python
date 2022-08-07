'''
Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python. Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python. Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.

FUNÇÕES PARTE I
 - DEF:
'''

'''def mostraLinha():
    print('------------------------------')


#PROGRAMA PRINCIPAL
mostraLinha()
print('     SISTEMA DE ALUNOS     ')
mostraLinha()
mostraLinha()
print('  CADASTRO DE FUNCIONÁRIOS  ')
mostraLinha()
mostraLinha()
print('     ERRO DO SISTEMA    ')
mostraLinha()'''

'''def mensagem(msg):
    print('--------------------')
    print(msg)
    print('--------------------')
mensagem('SISTEMA DE ALUNOS')'''


'''def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


título('  CURSO EM VIDEO  ')
título('  APRENDA PYTHON  ')
título('  GUSTAVO GUANABARA  ')'''


'''a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)'''

'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + b = {s}')


# programa principal
#soma(4, 5)
#soma(8, 9)
#soma(2, 1)
#soma(4)#dara erro, pois soma está recebendo na DEFINIÇÃO, DOIS parametros e não somente UM.
soma(4, 1)
soma(a=4, b=5)#os parametros podem ser explicitados, caso nao seja, NA DEFINIÇÃO automaticamente sera explicitado na sequencia
soma(b=4, a=5)#os parametros podem ser explicitados em qualuqer ordem, caso nao seja, NA DEFINIÇÃO automaticamente sera explicitado na sequencia
#soma(b=4, 5)#dara erro, pois a explicitação dos paramentros dve ser completa, OU referencia todos ou NÃO referencia nenhum.'''

#EMPACOTANDO PARAMETROS
'''def contador(*num):# * NUM informa que a DEF receberá varios parametros
    #print(num)
#impressão formatada
    for valor in num:
        print(f'{valor} - ', end='')
    print('FIM!')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''


#EMPACOTANDO PARAMETROS - TRABALHANDO COM TUPLAS
'''def contador(*num):# *NUM informa que a DEF receberá varios parametros
    #print(num)
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

#TRABALHANDO COM LISTA
'''def dobra(lst):#trabalhando com LISTA não é necessário utilizar (*NUM)
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)'''

#DESEMPACOTANDO PARAMETROS - TRABALHANDO COM TUPLAS
'''def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)'''


#FUNÇÕES SEM PARAMETROS
'''def lin():
    print('-' * 30)


lin()
print('  CURSO EM VIDEO  ')
lin()
print('  APRENDA PYTHON  ')
lin()
print('  GUSTAVO GUANABARA  ')
lin()

print('-----------------------=============================----------------')'''

#FUNÇÕES COM PARAMETROS
'''def titulo(txt):
    print('-' * len(txt))
    print(txt)
    print('-' * len(txt))


titulo('CURSO EM VIDEO')
titulo('APRENDA PYTHON')
titulo('GUSTAVO GUANABARA')'''


'''def soma(a, b, c=0):
    print(f'A vale {a}, B vale {b} e C vale {c}')
    s = a + b + c
    print(f'A soma entre A + B + C é igual a {s}')

#Programa Principal
soma(a=4, b=5)
soma(b=8, a=9)'''

#recebendo varios parametros
'''def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)