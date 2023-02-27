from datetime import date
ano_nasc = int(input('Ano de Nascimento do Atleta: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print('IDADE ATUAL: {}'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
