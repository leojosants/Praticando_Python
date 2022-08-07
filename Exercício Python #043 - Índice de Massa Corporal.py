'''Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 ate 30: Sobrepeso
- 30 ate 40: Obesidade
- Acima de 40: Obesidade Mórbida
IMC = p / alt * alt
'''

peso = float(input('Qual é seu peso (Kg)? '))
alt = float(input('Qual é sua altura? '))
imc = (peso / (alt * alt))
print('Seu IMC é {:.1f} \nSTATUS = '.format(imc), end='')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.8 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
elif imc >= 40:
    print('OBESIDADE MÓRBIDA')