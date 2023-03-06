from datetime import date
totmenor = 0
totmaior = 0
ano_atual = date.today().year
for c in range(1, 8):
    ano_nasc = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    if ano_atual - ano_nasc < 21:
        totmenor += 1
    else:
        totmaior += 1
print('Menores de Idade: {}'.format(totmenor))
print('Maiores de Idade: {}'.format(totmaior))
