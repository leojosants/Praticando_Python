'''DESAFIO 059 - crie um programa que leia dois valores e mostre um menu na tela:
- [1] - Somar
- [2] - Multiplicar
- [3] - Maior
- [4] - Novos numeros
- [5] - Sair do programa
Seu programa devera realizara operação solicitada em cada caso.'''
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    print('''
        [ 1 ]: Somar
        [ 2 ]: Multiplicar
        [ 3 ]: Maior
        [ 4 ]: Novos números
        [ 5 ]: Sair do programa''')
    opcao = int (input('>>>>>>> Escolha uma opção:' ))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} + {} é igual a {}.'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A resultado entre {} e {} é igual a {}.'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('O maior entre {} e {} é: {}'.format(n1, n2, maior))
        elif n2 > n1:
            maior = n2
            print('O maior entre {} e {} é: {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('DIGITE NOVOS NUMEROS')
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    else:
        print('Opção invalida... Tente novamente.')
print('PROGRAMA ENCERRADO')

