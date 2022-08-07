'''DESAFIO 024 - Verificando as primeiras letras de um texto Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao
com o nome "SANTO"'''

cid1 = str(input('Em qual cidade você nasceu? ')).strip()
print(cid1)
print('O nome da cidade contém a palavra "SANTO"? {}'.format("SANTO" in cid1))
print('O nome da cidade contém a palavra "SANTO"? {}'.format("SANTO" in cid1.upper())) #transformando todas as letras para masiusculo
