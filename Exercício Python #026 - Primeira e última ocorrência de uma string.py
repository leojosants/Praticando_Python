'''Faca um programa que leia uma frase pelo teclado: - Quantas vezes aparece a letra "A"; - Em que posição ela aparece a primeira vez; - Em que posição ela aparece a última vez'''
frase = str(input('Digite uma frase qualquer: ')).upper().strip()
print('A letra "A" aparece {} vezes na frase'.format(frase.count('A')))
print('A letra "A" aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra "A" aparece a ultima vez na posição {}'.format(frase.rfind('A')+1))#busca pelo lado direito