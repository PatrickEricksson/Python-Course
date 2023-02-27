print('CALCULADORA DE IMC')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
IMC = peso / (altura**2)
print('Seu IMC é {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Abaixo do Peso')
elif IMC <= 18.5 and IMC <= 25:
    print('Peso Ideal')
elif IMC <= 25 and IMC <= 30:
    print('Sobrepeso')
elif IMC <= 30 and IMC <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
