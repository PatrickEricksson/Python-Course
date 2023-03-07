soma_idade = 0
idade_mais_velho = 0
nome_mais_velho = ''
totmulheres = 0
for c in range(1,5):
    nome = str(input('Nome da {}º pessoa: '.format(c))).strip()
    idade = int(input('Idade: '))
    soma_idade += idade
    sexo = str(input('Sexo [M/F]: ')).strip()
    if sexo == 'M' and idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome
    if sexo == 'F' and idade < 20:
        totmulheres += 1
print('A média de idade do grupo é {}'.format(soma_idade/4))
print('O homem mais velho é {}, que tem {} anos'.format(nome_mais_velho, idade_mais_velho))
print('{} mulheres têm menos de 20 anos'.format(totmulheres))