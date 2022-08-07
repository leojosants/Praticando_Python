'''
Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort()). No final, mostre a lista ordenada na tela
'''
lista = []
for c in range(0, 5):#laco para cada c de 0 a 5
    n = int(input(f'Digite um valor para o {c+1}º índice: '))#solicita valor
    if c == 0 or n > lista[-1]:#verifica SE o contador for igua a zer OU se N for maior que o ultimo indice...
        lista.append(n)#...ira adicionar o numero
        print('\033[2;32mAdicionado ao final da lista...\033[m')
    else:# SENAO SE...
        pos = 0 #variavel iniciando com zero
        while pos < len(lista):#laco verificando, ENQUANTO a POS for menor que a quantidade de indices...
            if n <= lista[pos]:#..SE N for menor ou igual a POS no indice..
                lista.insert(pos, n) #... insira na POS tal um elemento N
                print(f'\033[2;34mAdicionado na posição {pos} da lista...\033[m')
                break#interrompe o laco SE N for menor ou igual a POS no indice..
            pos += 1# contagem de posição
print('-=-' * 30)
print(f'Os valores digitados foram ordenado da seguinte forma: {lista}')
