valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso...')
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Os valores adicionados foram {valores}')
print(f'Você digitou {len(valores)} valores')
valores.sort(reverse=True)
print(f'A lista de valores ordenada de forma descrescente é {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
