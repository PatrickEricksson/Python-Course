def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')

#Programa principal
maior(2, 9, 4, 5, 7, 1)