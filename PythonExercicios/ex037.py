num = int(input('Digite um número inteiro: '))
print('''Escolha a base de conversão:
[1] - Binário
[2] - Octal
[3] - Hexadecimal''')
option = int(input('Opção: '))
if option == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif option == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif option == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida')
