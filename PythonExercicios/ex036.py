valor = float(input('Valor da casa: R$ '))
sal = float(input('Salário do comprador: R$ '))
prazo = int(input('Em quantos anos vai pagar? '))
max_prest = sal * 0.30
actual_prest = valor / (prazo * 12)
print('Prestação Máxima: R$ {:.2f}'.format(max_prest))
print('Prestação Atual: R$ {:.2f}'.format(actual_prest))
if actual_prest > max_prest:
    print('EMPRÉSTIMO NEGADO! Parcela excede a capacidade de pagamento')
else:
    print('EMPRÉSTIMO APROVADO! Capacidade de pagamento suficiente')
