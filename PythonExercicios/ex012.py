preco = float(input('Preço do Produto: R$ '))
novo_preco = preco - (preco*0.05)
print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}'.format(preco, novo_preco))
