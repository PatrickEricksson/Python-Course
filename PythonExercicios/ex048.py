s = 0
for c in range(1,501):
    if c % 2 != 0 and c % 3 ==0:
        print(c)
        s += c
print('A soma dos números ímpares e múltiplos de 3 é {}'.format(s))
