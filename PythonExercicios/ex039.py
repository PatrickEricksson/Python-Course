from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Digite seu ano de nascimento: '))
idade = ano_atual-ano_nasc
print('Sua idade é de {} anos'.format(idade))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    prazo = 18 - idade
    print('Ainda vai se alistar. Faltam {} anos para o alistamento'.format(prazo))
else:
    prazo = idade - 18
    print('Já se passaram {} anos do tempo de alistamento'.format(prazo))
