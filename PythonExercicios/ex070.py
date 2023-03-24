tot = totmil = menor = cont = 0
barato = ''
print('-' * 30)
print('LOJA SUPER BARATÃO')
print('-' * 30)
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    tot += preco
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    if preco > 1000:
        totmil += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R$ {tot:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1.000')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')