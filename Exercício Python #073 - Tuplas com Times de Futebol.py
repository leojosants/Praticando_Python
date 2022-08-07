'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: A) - Apenas os 5 primeiros colocados; B) - Os ultimos 4 colocados da tabela; C) - Uma lista com os times em órdem alfabética; D) - Em que posição na tabela está o time da Chapecoense.
'''

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
         'Atlético', 'Atlético - PR', 'Cruzeiro', 'Botafogo', 'Santos',
         'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará-SC',
         'Vasco da Gama', 'Sport Recife', 'América-MG', 'EC Vitória', 'Paraná')
print(f'Os cinco primeiros colocados da tabela são = {times[:5]}')
print(f'Os ultimos 4 colocados da tabela são = {times[-4:]}')
print(f'Todos os times da tabela ordenados em órdem alfabética = {sorted(times)}')
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª da tabela.')

#for pos, t in enumerate(times):
    #print(pos, t)