matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
totpar = totcoluna3 = maiorlinha2 = 0
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            totpar += matriz[l][c]
        if c == 2:
            totcoluna3 += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maiorlinha2:
                maiorlinha2 = matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {totpar}')
print(f'A soma dos valores da terceira coluna é {totcoluna3}')
print(f'O maior valor da segunda linha é {maiorlinha2}')
