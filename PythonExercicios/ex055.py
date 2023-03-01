menor_peso = 9999
maior_peso = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(c)))
    if peso <= menor_peso:
        menor_peso = peso
    if peso >= maior_peso:
        maior_peso = peso
print('O MENOR peso é {} Kg'.format(menor_peso))
print('O MAIOR peso é {} Kg'.format(maior_peso))