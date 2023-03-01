valor = float(input('Valor da casa: R$ '))
sal = float(input('Salário do comprador: R$ '))
prazo = int(input('Em quantos anos vai pagar? '))
actual_prest = valor / (prazo * 12)
print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação é de R$ {:.2f}'.format(valor, prazo, actual_prest))
max_prest = sal * 0.30
print('Prestação Máxima: R$ {:.2f}'.format(max_prest))
if actual_prest > max_prest:
    print('EMPRÉSTIMO NEGADO! Parcela excede a capacidade de pagamento')
else:
    print('EMPRÉSTIMO APROVADO! Capacidade de pagamento suficiente')
