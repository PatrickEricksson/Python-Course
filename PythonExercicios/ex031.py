dist = float(input('Digite a distância da viagem: '))
print('Você está prestes a começar uma viagem de {} Km'.format(dist))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print('Preço da Passagem: R$ {:.2f}'.format(preco))
