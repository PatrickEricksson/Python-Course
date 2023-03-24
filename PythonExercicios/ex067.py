while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    print('TABUADA DO {}'.format(n))
    print('-' * 12)
    for c in range(1, 11):
        print(f'{n} X {c:2} = {n*c}')
    print('-' * 12)
print('Programa Tabuada ENCERRADO! Volte sempre!')