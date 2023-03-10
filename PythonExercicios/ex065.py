resp = 'S'
media = soma = cont = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont +=1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
