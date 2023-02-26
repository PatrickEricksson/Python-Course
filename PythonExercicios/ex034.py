sal_atual = float(input('Salário Atual: R$ '))
if sal_atual > 1250:
    sal_novo = sal_atual * 1.10
else:
    sal_novo = sal_atual * 1.15
print('Novo Salário: R$ {:.2f}'.format(sal_novo))
