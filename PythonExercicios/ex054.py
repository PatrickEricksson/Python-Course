from datetime import date
menor = 0
maior = 0
ano_atual = date.today().year
for c in range(1, 8):
    ano_nasc = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    if ano_atual - ano_nasc < 21:
        menor = menor + 1
    else:
        maior = maior + 1
print('Menores de Idade: {}'.format(menor))
print('Maiores de Idade: {}'.format(maior))
