soma_idade = 0
for c in range(1,5):
    nome = str(input('Nome da {}º pessoa: '.format(c)))
    idade = int(input('Idade: '))
    soma_idade += idade
    sexo = str(input('Sexo [M/F]: '))
print('A média da idade do grupo é {}'.format(soma_idade/4))
