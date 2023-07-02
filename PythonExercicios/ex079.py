valores = list()
while True:
    num = int(input('Digite um número: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor já cadastrado. Não foi adicionado!')
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Os valores adicionados foram {valores}')