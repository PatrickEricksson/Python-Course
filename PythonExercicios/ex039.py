from datetime import date
ano_nasc = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual-ano_nasc
print('Sua idade é de {} anos'.format(idade))
if idade < 18:
    prazo = 18 - idade
    print('Ainda vai se alistar. Faltam {} anos para o alistamento'.format(prazo))
elif idade == 18:
    print('Hora de se alistar')
else:
    prazo = idade - 18
    print('Já se passaram {} anos do tempo de alistamento'.format(prazo))
