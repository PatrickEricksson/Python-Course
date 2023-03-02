t1 = int(input('Primeiro termo: '))
p = int(input('Progressão: '))
decimo = t1 + (10 - 1) * p
for c in range(t1, decimo + p, p):
    print('{}'.format(c), end=' - ')
print('ACABOU')