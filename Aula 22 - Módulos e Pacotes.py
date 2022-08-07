'''Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo como criar módulos em Python e reutilizar nossos códigos em outros projetos. Vamos aprender também como agrupar vários módulos em um pacote, ampliando ainda mais a modularização em grandes projetos em Python.'''

'''
        MÓDULOS E PACOTES

--->>> Modularização

- Surgiu no início da década de 60.
- Sistemas ficando cada vez maiores.
- Foco: - Dividir um programa grande.
        - Aumentar a legibilidade.
        - Facilitar a manutenção.

___________________________________________________

def fatorial(n):
    f = 1
    for c in range(1, num+1):
        f *= c
    return f

# Programa Principal
num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')

___________________________________________________

-> Vantagens Modularização

- Organização do código.
- Facilidade na manutenção.
- Ocultação do código detalhado.
- Reutilização em outros projetos (Basta copiar a pasta dentro de outros projetos)
_______________________________________________________________________________________________

--->>> Pacotes

- Criação: - Dentro do projeto, criar um pacote (PYTHON PACKAGE) e nomear de "uteis"
           - OBS: ANTES, EXLCUIR O ARQUIVO "UTEIS.PY"
           - Dentro do pacote criado, criar um novo pacote chamado "NUMEROS"

'''