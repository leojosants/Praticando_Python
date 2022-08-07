'''105: Faça um programa que tenha uma função notas() que pode receber várias notas
de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
- Adicione as docstrings'''

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos
    :param n: Uma ou mais notas dos alinos, aceita várias
    :param sit: Valor opcional, indicando se deve ou nao adicionar a situação
    :return: Dicionario com varias informações
    """
    r = dict() # OU r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['manor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'

    return r

# Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)