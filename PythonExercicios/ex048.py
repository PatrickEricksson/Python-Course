s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        s += c
        cont += 1
print('A soma dos {} números ímpares e múltiplos de 3 é {}'.format(cont, s))
