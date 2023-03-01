from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Ano de Nascimento do Atleta: '))
idade = ano_atual - ano_nasc
print('IDADE ATUAL: {} anos'.format(idade))
if idade <= 9:
    print('Classificado: MIRIM')
elif idade <= 14:
    print('Classificado: INFANTIL')
elif idade <= 19:
    print('Classificado: JUNIOR')
elif idade <= 25:
    print('Classificado: SÊNIOR')
else:
    print('Classificado: MASTER')
