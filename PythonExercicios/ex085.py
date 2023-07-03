lista = []
pares = []
impares = []
for c in range(1, 8):
    n = int(input(f'Digite o {c} valor: '))
    if n % 2 == 0:
        pares.append(n)
        lista.append(pares[:])
    elif n % 2 == 1:
        impares.append(n)
        lista.append([impares])
