lista = []
dados = []
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    lista.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Os dados foram {lista}')
print(f'Ao todo você cadastrou {len(lista)} pessoas')
print(f'O maior peso foi de {mai} KG. Peso de ', end='')
for p in lista:
    if p[1] == mai:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {men} KG. Peso de ', end='')
for p in lista:
    if p[1] == men:
        print(f'{p[0]} ', end='')
print()