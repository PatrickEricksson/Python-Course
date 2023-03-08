print('Gerador de PA')
print('-=' * 10)
t = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} -> '.format(t), end='')
        t += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
