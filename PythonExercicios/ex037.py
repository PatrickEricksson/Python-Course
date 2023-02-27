num = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão: '
      '1 - Binário'
      '2 - Octal'
      '3 - Hexadecimal')
option = int(input('Opção: '))
if option == 1:
    new_num = bin(num)
elif option == 2:
    new_num = oct(num)
elif option == 3:
    new_num = hex(num)
