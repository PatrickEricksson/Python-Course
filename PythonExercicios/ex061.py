print('Gerador de PA')
t = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
c = 1
while c <= 10:
    print('{} -> '.format(t), end='')
    t += r
    c += 1
print('FIM')
