while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        print('Programa Tabuada ENCERRADO! Volte sempre!')
        break
    print('TABUADA DO {}'.format(n))
    print('-' * 12)
    for c in range(0, 11):
        print(f'{n} X {c:2} = {n*c}')
    print('-' * 12)
