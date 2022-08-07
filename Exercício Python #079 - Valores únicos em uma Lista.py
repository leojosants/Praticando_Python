'''
Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista. Caso o numero ja exista la dentro, ele nao será adicionado. No final, serão exibidos todos os valores unicos digitados, em ordem crescente.
'''
val = []
while True:
    n = int(input('Digite um valor: '))
    if n not in val:#verifica se o numero digitado ja consta na lista
        val.append(n)#caso nao contar na lista ele será adicionado
        print('\033[2;34mValor adicionado com SUCESSO\033[m')
        val.sort()
    else:
        print('\033[7mVALOR DUPLICADO...Nao adicionado\033[m')
    resp = ' '
    while resp not in 'SN':# verifica se a resposta é S ou N, enquanto a resposta nao for S ou N, ficara perguntando
        resp = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if resp == 'N':#condição de saida se a resposta for NAO
        break
print(f'Os valores digitados e ordenados foram {val}')