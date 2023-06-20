num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.insert(2, 0)
print(num)
num.pop() # O POP sozinho elimina o último número
print(num)
num.pop(2)
print(num)
num.remove(2) #Elimina o primeiro elemento 2. Se tiver número repetido, elimina o primeiro
print(num)
if 5 in num:
    num.remove(5)
    print('Removi o número 5')
else:
    print('Não achei o número 5')
print(num)
print('-----NOVO EXERCÍCIO-----')
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
print('-----NOVO EXERCÍCIO-----')
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')