'''from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
print('O fatorial de {} é {}'.format(num, factorial(num)))'''

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c # Faz a conta do fatorial
    c -= 1 # Faz o contador avançar para o próximo número
print('{}'.format(f))
