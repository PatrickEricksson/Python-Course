import os

print('=' * 20)
operations = {
    "+": "Soma",
    '+': 'Adição',
    '-': 'Subtração',
    'x': 'Multiplicação',
    '/': 'Divisão',
    '^': 'Exponenciação'
}

while True:
    os.system("cls")
    i = 0
    for op, name in operations.items():
        print(i, ':', name)
        i += 1
    print()
    op = int(input('Escolha a operação que deseja realizar: '))
    op_string = list(operations.keys())[op]
    
    print()
    print(f'>>> {op_string} escolhida')
    print()
    v1 = float(input('Qual o primeiro valor? '))
    v2 = float(input('Qual o segundo valor? '))

    if op == 0:
        result = v1 + v2
    elif op == 1:
        result = v1 - v2
    elif op == 2:
        result = v1 * v2
    elif op == 3:
        result = v1 / v2
    elif op == 4:
        result = v1 ** v2

    print()
    print(f'{v1} {op_string} {v2} = {result}')
    print()
    print('=' * 20)
    resp = int(input('Deseja fazer mais alguma operação? 0 - SIM, 1 - NÃO '))
    if resp == 1:
        break
