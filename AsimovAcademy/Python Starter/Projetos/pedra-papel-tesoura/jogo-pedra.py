import random
import os

def clear_screen():
    if os.name == 'nt': #Para sistemas Windows
        os.system('cls')
    else: #Para sistemas Unix/Linux/Mac
        os.system('clear')
        
def get_user_choice():
    while True:
        print('Escolha:\n0 - Pedra\n1 - Papel\n2 - Tesoura')
        try:
            user_choice = int(input())
            if user_choice in (0, 1, 2):
                return user_choice
            else:
                print('Número inválido! Tente novamente.')
        except ValueError:
            print('Entrada inválida! Digite um número inteiro!')
            
def get_computer_choice():
    choices = [0, 1, 2]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Empate'
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return 'Você venceu!'
    else:
        return 'Computador venceu!'
    
def play_again():
    print('Quer jogar novamente? [S/N]')
    return input().lower().startswith('s') #Se o jogador digitar "s" ou qualquer entrada que começe com "s" (como "sim", "S", "Sim", etc) a função retorna True

def main():
    player_wins = 0
    computer_wins = 0
    print('=========================================')
    print('Bem vindo ao Jogo Pedra, Papel e Tesoura!')
    print('=========================================')
    
    while True:
        print('PLACAR: ')
        print(f'Você: {player_wins}')
        print(f'Computador: {computer_wins}')
        print()
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        choices_dict = {0: 'Pedra', 1: 'Papel', 2: 'Tesoura'}
        print(f'Você escolheu: {choices_dict[user_choice]}')
        print(f'O computador escolheu: {choices_dict[computer_choice]}')

        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == 'Você venceu!':
            player_wins += 1
        elif result == 'Computador venceu!':
            computer_wins += 1
        
        if not play_again(): #Se o resultado da função for False, pausa o programa
            break
    
        clear_screen()
    print('Obrigado por jogar!')

if __name__ == "__main__":
    main()
    