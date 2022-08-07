'''DESAFIO 042 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC(peso / alt * alt)  e mostre o status,
de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30 : Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade morbida'''

pes = float(input('Digite seu peso (Kg): '))
alt = float(input('Digite sua altura (metros): '))
imc = (pes / (alt ** 2))# comando que calcula a altura ao quadrado
print('Seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 < imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
