resp = 'S'
tot18 = totaH = totM20 = 0
while True:
    print('-' * 12)
    print('CADASTRE UMA PESSOA')
    print('-' * 12)
    idade = int(input('Idade: '))
    if idade > 18:
        tot18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        totaH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    print('-' * 12)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totaH} homens cadastrados')
print(f'Temos {totM20} mulheres com menos de 20 anos')
