'''102: Crie um programa que tenha uma função fatorial() que receba dois
parâmetros: o primeiro que indique o número a calcular e outro chamado
show, que será um valor lógico (opcional) indicando se será mostrado ou não
na tela o processo de cálculo do fatorial.'''

def fatorial(num = 0, show=False):
    """
    -> Calcula o fatorial de um numero
    :param a: Número a ser calculado
    :param b: (Opcional)
    :return: O fatorial de um numero n
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# Programa Principal
print(fatorial(5, show=True))
help(fatorial)