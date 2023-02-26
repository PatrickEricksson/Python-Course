vel = float(input('Qual é a velocidade atual do carro: '))
if vel > 80:
    print('Você foi multado! Limite de 80 km/h excedido!')
    multa = (vel - 80) * 7
    print('Você deve pagar uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
