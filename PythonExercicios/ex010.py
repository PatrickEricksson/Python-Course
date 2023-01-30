real = float(input('Quantos reais você tem na carteira? R$ '))
dolar = real / 3.27
print('Com R$ {} você pode comprar ${:.2f} dólares'.format(real, dolar))
