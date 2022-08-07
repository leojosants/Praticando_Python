'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do Jogador: '))
totpart = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for c in range(0, totpart):
    partidas.append(int(input(f'Gol(s) na partida {c+1}: ')))
jogador['gols'] = partidas[:]
jogador['tot gols'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["tot gols"]} gols.')