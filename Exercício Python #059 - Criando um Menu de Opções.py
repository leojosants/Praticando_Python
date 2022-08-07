'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] - Somar; [2] - Multiplicar; [3] - Maior; [4] - Novos numeros; [5] - Sair do programa.
Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep# imporatação da biblioteca time somente o metodo sleep
n1 = int(input('Primeiro valor: '))# solicitando valor
n2 = int(input('Segundo valor: '))# solicitando valor
opc = 0#variavel iniciando com zero
while opc != 5:# enquanto opçaõ não for igual a 5
    print('''    [ 1 ] = Somar
    [ 2 ] = Multiplicar
    [ 3 ] = Maior
    [ 4 ] = Novos números
    [ 5 ] = Sair do programa''')
    opc = int(input('>>>>> Qual é sua opção? '))# solicitando opção
    if opc == 1:# se opção igual a um
        s = n1 + n2# variavel S recebendo o resultado da soma entre N1 e N2
        print('A soma entre {} e {} é {}.'.format(n1, n2, s))#print do resultado da soma entre n1 e n2
    elif opc == 2:# senao se opção igual 2
        m = n1 * n2# variavel M recebendo o resultado da multiplicação entre N1 e N2
        print('O resultado de {} x {} é {}'.format(n1, n2, m))#print do resultado da multiplicação entre N1 e N2
    elif opc == 3:# senao se opção igual a
        if n1 > n2:#se N1 for MAIOR que N2
            maior = n1# varial MAIOR recebe N1
        else:# senao
            maior = n2# variavel MAIOR recebe N2
        print('Entre {} e {}, o maior valor é {}.'.format(n1, n2, maior))# print do resultado de qual é o MAIOR entre N1 e N2
    elif opc == 4:# senao se opção igual a 4
        print('Informe os numeros novamente: ')# printe informação
        n1 = int(input('Primeiro valor: '))# solicita valor
        n2 = int(input('Segundo Valor: '))# solicita valor
    elif opc == 5:#senao se opção igual a 5
        print('Finalizando...')# print informação
    else:# senao
        print('Opção inválida. Tente novamente.')# print informação
    print('=-=' * 10)# print informação
    sleep(1)#metodo pausa de 1 segundo
print('Fim do programa! Volte sempre!')# print informação