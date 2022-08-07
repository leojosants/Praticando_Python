def aumentar(preco=0, taxa=0):
    res = preco + (preco * taxa / 100)
    return res


def diminuir(preco=0, taxa=0):
    res = preco - (preco * taxa / 100)
    return res


def dobro(preco=0):
    res = preco * 2
    return res


def metade(preco=0,):
    res = preco / 2
    return res

def moeda(preco=0, moeda='R$'): # moeda nesse cado é um paramentro
    return f'{moeda}{preco:.2f}'.replace('.', ',') #REPLACE SUBSTITUIR TODOS OS PONTOS POR VIRGULA
