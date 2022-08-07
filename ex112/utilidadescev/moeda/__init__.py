def aumentar(preco=0, taxa=0, formato=False):
    """
    ->
    :param preco:
    :param taxa:
    :param formato:
    :return:
    """

    res = preco + (preco * taxa / 100)

    return res if formato is False else moeda(res) # COM o operador "IN" que substitui o "==" será return res if formato is False else moeda(res)

   #return res if not formato else moeda(res)      # SEM o operador "IS" que substitui o "==" será return res if not formato else moeda(res)



def diminuir(preco=0, taxa=0, formato=False):
    """
    ->
    :param preco:
    :param taxa:
    :param formato:
    :return:
    """

    res = preco - (preco * taxa / 100)

    return res if formato is False else moeda(res)



def dobro(preco=0, formato=False):
    """
    ->
    :param preco:
    :param formato:
    :return:
    """

    res = preco * 2

    return res if formato is False else moeda(res)



def metade(preco=0, formato=False):
    """
    ->
    :param preco:
    :param formato:
    :return:
    """

    res = preco / 2

    return res if formato is False else moeda(res)



def moeda(preco=0, moeda='R$'): # moeda nesse caso é um paramentro
    """
    ->
    :param preco:
    :param moeda:
    :return:
    """

    return f'{moeda}{preco:.2f}'.replace('.', ',') #REPLACE SUBSTITUIR TODOS OS PONTOS POR VIRGULA


def resumo(preco=0, taxaA=10, taxaD=5):
    """

    :return:
    """
    print('-'*30)
    print('RESUMO DO VALOR'.center(30)) # CENTER centraliza os caracteres
    print('-'*30)

    print(f'Preço analisado: \t{moeda(preco)}') # Contra barra T "\t" realiza tabulação
    print(f'Dobro do preço: \t{dobro(preco,True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaA}% de aumento: \t{aumentar(preco, taxaA, True)}')
    print(f'{taxaD}% de redução: \t{diminuir(preco, taxaD, True)}')
    print('-'*30)