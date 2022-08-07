'''DESAFIO 073 - Crie uma tupla preenchida com os 20 primeiros colocados da
tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
- Apenas os 5 primeiros colocados.
- Os ultimos 4 colocados da tabela.
- Uma lista com os nomes em ordem alfabética.
- Em que posição na tabela está o time da chapecoense'''

'''tabela = ('Flamengo', 'internacional', 'AtleticoMG', 'São Paulo', 'Fluminense',
          'Grêmio', 'Palmeiras', 'Santos', 'AtleticoPR', 'Corinthians',
          'Bragantino', 'CearáSC', 'AtleticoGO', 'Sport RC', 'Bahia',
          'Fortaleza', 'Vasco', 'Goias', 'Chapecoense', 'Botafogo')'''
tabela = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
          'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
          'Atletico', 'Botafogo', 'AtleticoPR', 'Bahia',
          'São Paulo', 'Fluminense', 'Sport Recife',
          'EC Vitoria', 'Coritiba', 'Avai', 'Ponte Preta',
          'AtleticoGO')
for time in range(0, len(tabela)):
    print(f'{time+1}ª posição: ', tabela[time])
print('-='*15)
#print(f'Lista de times: {tabela}')
print(f'- Cinco primeiros colocados: {tabela[:5]}')
print('-='*15)
print(f'- Ultimos 4 colocados: {tabela[-4:]}')
print('-='*15)
print(f'- Times em ordem alfabetica: {sorted(tabela)}')
print('-='*15)
print(f'O Chapecoense está no índice: {tabela.index("Chapecoense")}', end=' ')# DENTRO DO INDEX, UTILIZAR ASPAS DUPLAS
print(f'e na posição: {tabela.index("Chapecoense")+1}')# DENTRO DO INDEX, UTILIZAR ASPAS DUPLAS
