menor_peso = 0
maior_peso = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(c)))
    if c == 1:
        menor_peso = peso
        maior_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print('O MENOR peso é {} Kg'.format(menor_peso))
print('O MAIOR peso é {} Kg'.format(maior_peso))
