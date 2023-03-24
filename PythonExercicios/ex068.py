from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
jogador = int(input('Digite um valor: '))
resp_jogador = str(input('Par ou Ímpar? [P/I] '))
if resp_jogador == 'P':
    resp_computador = 'I'
else:
    resp_computador = 'P'
computador = randint(0, 10)
soma = jogador + computador
if soma % 2 == 0:
    resultado = 'PAR'
else:
    resultado - 'ÍMPAR'
print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU {resultado}')
