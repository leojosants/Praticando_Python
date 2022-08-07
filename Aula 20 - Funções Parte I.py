'''Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python. Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python. Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.'''

'''print('-'*30)
print('  CURSO EM VÍDEO  ')
print('-'*30)
print('-'*30)
print('  APRENDA PYTHON  ')
print('-'*30)
print('-'*30)
print('  GUSTAVO GUANABARA  ')
print('-'*30)'''


#OUTRO PROGRAMA
'''def lin():
    print('-' * 30)

#PROGRAMA PRINCIPAL
lin()
print('  CURSO EM VÍDEO  ')
lin()
print('  APRENDA PYTHON  ')
lin()
print('  GUSTAVO GUANABARA  ')
lin()
print('FIM')
print()'''


#OUTRO PROGRAMA
'''def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)
mensagem('SISTEMA DE ALUNOS')'''


#OUTRO PROGRAMA
'''def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

#Programa Principal
titulo('  CURSO EM VÍDEO  ')
titulo('  APRENDA PYTHON  ')
titulo('  GUSTAVO GUANABARA  ')
titulo('  PYTHON É MUITO BOM!  ')
titulo('OI')'''


#OUTRO PROGRAMA
'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A+B é: {s}')

#Programa Principal
soma(4, 5) #SEM EXPLICITAR QUEM A E B, AUTOMATICAMENTE 4 É A E 5 É B
soma(a=4, b=5) #OU
soma(b=4, a=5) #INVERTENDO PARAMENTRO ENTRE A E B
soma(7, 2)
#soma(3, 9, 5) #declarando 3 valores e definindo somente dois, dará erro
#soma(8, 9)
#soma(2, 1)
#soma(4, 1)'''

#OUTRO PROGRAMA
'''def contador(*num): # *num recebe vários parametros
    #print(num)
    #print formatado
  #  for valor in num:
        print(f'{valor}', end=' ')
  #  print('FIM!')
  #  #print(len(num))
  #  tan = len(num)
  #  print(f'Recebi os valores {num} e são ao todo {tan} numeros.')

#programa Principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''


#OUTRO PROGRAMA
'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


#Programa Principal
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
print(len(valores))'''

#
'''def mostraLinha():
    print('-'*30)


mostraLinha()#print('-'*30)
print('SISTEMAS DE ALUNOS')
mostraLinha()#print('-'*30)

mostraLinha()#print('-'*30)
print('CADASTRO DE FUNCIONARIOS')
mostraLinha()#print('-'*30)

mostraLinha()#rint('-'*30)
print('ERRO DO SISTEMA')
mostraLinha()#print('-'*30)'''

#
'''print('-'*30)
print('  CURSO EM VÍDEO')
print('-'*30)

print('-'*30)
print('  APRENDA PYTHON')
print('-'*30)

print('-'*30)
print('  GUSTAVO GUANABARA')
print('-'*30)'''


#
'''def lin():
    print('-'*30)


lin()
print('   CURSO EM VIDEO')
lin()
print('  APRENDA PYTHON')
lin()
print('  GUSTAVO GUANABARA')
lin()'''


#TRABALHANDO COM PARÂMETROS
'''print('-'*30)
print('   SISTEMA DE ALUNOS')
print('-'*30)

print('-'*30)
print('   CADSTRO DE FUNCIONÁRIOS')
print('-'*30)

print('-'*30)
print('   ERRO DO SISTEMA')
print('-'*30)'''


#
'''def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)

mensagem('   SISTEMA DE ALUNOS')
mensagem('CADASTRO DE FUNCIONARIOS')
mensagem('ERRO DO SISTEMA')'''


#
def soma(a, b):
    print(f'A= {a} e B= {b}')
    s = a + b
    print(f'A soma entre A= {a} e B= {b} é {s}')
    print('-'*30)


# Programa Principal
soma(4, 5) # O primeiro valor vai pra A e o segundo vai para B # OU
soma(a = 4, b = 5) # pode informa que o paramentro A sera 4 e B será 5
soma(a = 5, b = 4) # pode informar o valor alterado de A ser 5 e B ser 4
# a = 4 # b = 5 # s = a + b # print(s)
soma(8, 9) # OU
soma(a = 8, b = 9)
# a = 8 # b = 9 # s = a + b # print(s)
soma(2, 1) # OU
soma(a = 2, b = 1)
# a = 2 # b = 1 # s = a + b # print(s)
#soma(3, 9, 0) # informando valores a mais do que o parametro dará erro, para corrigir informe o parametro como (*), que recebera varios dados


# TRABALHANDO COM EMPACOTAMENTO / DESEMPACOTAMENTO
'''def contador(*num):
    #print(num) # haverá a criação de uma TUPLA
    #for c in num:
     #   print(num, end=' ')
    #print('FIM')
    tan = len(num)
    print(f'Recebi os valores de {num} e são ao todo {tan} numeros.')

# Programa Principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''


#
'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

# Programa Principal
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)'''


#
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

# Programa Principal
soma(5, 2)
soma(2, 9, 4)