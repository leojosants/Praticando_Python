'''Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio
104, incluindo agora a possibilidade da digitação de um número de tipo
inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor digite um número inteiro válido. \033[m')
            continue # comando que se der a exceção acima, ele retorna ao While tru
        except KeyboardInterrupt:
            print('Entrada interrompida pelo usuário.')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO. Por favor digite um número Real.\033[m')
            continue
        except KeyboardInterrupt:
            print('Entradada interrompida pelo usuário.')
            return 0
        else:
            return n


# Programa Principal
n1 = leiaInt('Digite um numero Inteiro: ')
n2 = leiaFloat('Digite um número Real: ')
print(f'O valor Inteiro digitado foi {n1} e o número Real digitado foi {n2}')