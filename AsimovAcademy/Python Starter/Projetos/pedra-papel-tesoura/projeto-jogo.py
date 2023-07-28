import random
import os

move_list = ['papel', 'pedra', 'tesoura']
player_count = 0
computer_count = 0

print('========================================')
print('Bem vindo ao jogo Papel, Pedra e Tesoura')


def main_print():
    print('========================================')
    print('\nPLACAR: ')
    print(f'Você: {player_count}')
    print(f'Computador: {computer_count}')
    print()
    print('Escolha seu lance: ')
    print('0 - Papel | 1 - Pedra | 2 - Tesoura')
    
def select_move():
    return random.choice(move_list)

def get_player_move():
    while True:
        try:
            player_move = int(input('Lance: '))
            if player_move not in [0, 1, 2]:
                raise
            return move_list[player_move]
        
        except Exception as e:
            print(e)
            
def select_winner(p_move, c_move):
    global player_count, computer_count
    if p_move == 'papel':
        if c_move == 'pedra':
            player_count += 1
            return 'p'
        if c_move == 'tesoura':
            computer_count += 1
            return 'c'
        else:
            return 'd'
        
    if p_move == 'pedra':
        if c_move == 'tesoura':
            player_count += 1
            return 'p'
        if c_move == 'papel':
            computer_count += 1
            return 'c'
        else:
            return 'd'

    if p_move == 'tesoura':
        if c_move == 'papel':
            player_count += 1
            return 'p'
        if c_move == 'pedra':
            computer_count += 1
            return 'c'
        else:
            return 'd'

again = 1
while again == 1:
    main_print()
    player_move = get_player_move()
    computer_move = select_move()
    winner = select_winner(player_move, computer_move)
    
    print()
    print('=' * 20)
    print(f'Sua jogada: {player_move}')
    print(f'Jogada do Computador: {computer_move}')

    if winner == 'p':
        print('Você venceu!')
    elif winner == 'c':
        print('Você perdeu!')
    else:
        print('Empate')
    print('=' * 20)
    
    while True:
        print('Jogar Novamente? 0 - SIM | 1 - NÃO')
        next = int(input())
        if next == 0:
            break
        elif next == 1:
            again = 0
            break
    os.system('cls')