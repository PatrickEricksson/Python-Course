t1 = int(input('Primeiro termo: '))
r = int(input('Progressão: '))
decimo = t1 + (10 - 1) * r
for c in range(t1, decimo + r, r):
    print('{}'.format(c), end=' - ')
print('ACABOU')