'''DESAFIO 080: Crie um programa onde o usuário possa digitar cinco
valores numéricos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela'''

'''valores = []
ordenada = []
maior = menor = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    valores.append(n)
print(f'A lista criada foi {valores}')
for c, v in enumerate(valores):
    if c == 0:
        maior = menor = n = 0
    else:
        if maior > n:
            maior = n
            print(f'Valor adicionado na {c} posição')'''

lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: #Verifica se o primeiro valor digitado é igual e zero ou se ele é maior que o ultimo numero da lista.
        lista.append(n)
        print('Adicinoado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram: {lista}')
