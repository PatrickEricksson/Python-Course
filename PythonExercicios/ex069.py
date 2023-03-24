resp = 'S'
while resp == 'S':
    print('-' * 12)
    print('CADASTRE UMA PESSOA')
    print('-' * 12)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] '))
    print('-' * 12)
    resp = str(input('Quer continuar? [S/N]'))
