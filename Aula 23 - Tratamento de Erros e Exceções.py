''' Aula 23 – Tratamento de Erros e Exceções
Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções. Aprenda como usar a estrutura try except no Python de uma forma simples.
'''

#primt(x) # A EXCEÇÃO FOI: NameError: name 'primt' is not defined -  Erro de sintaxe, "M" no lugar de "N"

#print(x) # A EXCEÇÃO FOI: NameError: name 'x' is not defined - Erro de significado - A variável "x" não foi definida ainda

'''
x = 8
print(f'{x}')
'''

'''
n = int(input('Número: '))
    # caso digite o valor por extenso, esse valar é uma string e dará uma EXCEÇÃO chamada ValueError: invalid literal for int() with base 10: 'oito', pois o valor pedido foi inteiro (INT)
print(f'Você digitou o número {n}')
'''

'''
a = int(input('Numerador: '))
b = int(input('Denominador: '))
    # Caso digite "o numero ZERO" no denominador, dará uma EXCEÇÃO chamada ZeroDivisionError: division by zero, pois na matemática qualquer numero dividido por zero é zero
    # Caso digite uma string em qualquer variável, ocorrerá uma EXCEÇÃO chamada ValueError: invalid literal for int() with base 10: 'e', pois o solicitado foi um numero inteiro
    # Caso digite nao digite nada qualquer variável, ocorrerá uma EXCEÇÃO chamada ValueError: invalid literal for int() with base 10: pois o solicitado foi um numero inteiro
#r = a / b
r = 2/'2'
print(f'O resultado é {r}')
'''

'''
r = 2 / '2'
    # Ocorrerá uma EXEÇÃO chamada TypeError, pois o dividendo (2 é um número inteiro) e o divisor '2' é uma STRING, sendo tipos diferentes
print(r)
'''

'''lst = [3, 6, 4]
    # Ocorrerá uma EXEÇÃO chamada IndexError (quando é listas) em dicionários é (Keyerror), pois na variavel LST não possui o indice 3, somente os indices 0, 1, 2
print(lst[3]) # Solicita impressão na tela do indice 3, que inclusive não existe
'''

'''
import uties
    #Caso o módulo não existe, ocorrerá uma EXCEÇÃO chamada ModuleNotFoundError, que significa erro de módulo não encontrado.
'''

# Busca no Google e verifica a quantidade de EXCEÇÕES existentes:
    # python exception
    # python exception list

# Exception: Siginifica exceção, porém um erro que não ocorre sempre

'''COMANDO PARA TRATAMENTO DE ERROS'''

'''
try: # Signficado "TENTE alguma coisa senão acontece uma exceção, que é o comando except"
    OPERAÇÃO # Digitar nesse campo os comando que normalmente dão problema
except: # Busca a EXCEÇÃO
    FALHOU # Significa "se eu tenta a coisa de cima, o vai acontecer?"
--> Um mesmo TRY pode ter vários EXCEPT para tratar cada erro, ex:
   -> except Typeerror:
        print()
   -> except ValueError:
        print()
   -> except OSError:
        print()
except Exception as erro: # Comando que mostra o tipo de erro. Ex cause, class, context etc.
    print(f'O probela encontrado foi {erro}')
else: # caso não dê problema - (Comando opcional)
    DEU CERTO
finally: # Acontecerá independente se DEU CERTO ou se DEU ERRO - (Comando opcional de finalização)
    CERTO/FALHA
'''

try: # TENTAR
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
#except: # SE DER PROBLEMA --> Pode ser usado um comando para receber, mostrar e tratar o erro utilizando 'except Exception as erro'
    #print(f'Infelismente tivemos um problema')
except (ValueError, TypeError):# Para colocar mais de um erro, basta colocá-los dentro de parenteses e separar por virgula.
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados. ')
#except Exception as erro:  # Comando que mostra o tipo de erro. Ex cause, class, context etc.
    #print(f'Problema encontrado foi {erro.__cause__}')
else: # SE NAO DER PROBLEMA
    print(f'O resultado é {r:.1f}')
finally: # FINALIZAÇÃO
    print('Volte sempre! Muito obrigado')