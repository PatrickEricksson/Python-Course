import os
import random
from time import sleep

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Verificar linhas, colunas e diagonais
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)): # Verifica Linhas e colunas
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)): # Verifica Diagonais
        return True
    return False
  
def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

def get_player_move(player):
    while True:
        try:
            
            row = int(input(f"Jogador {player}, escolha a linha (0, 1 ou 2): ")) # Solicita ao jogador para escolher a linha
            if row not in [0, 1, 2]: # Verifica se a entrada da linha é válida (0, 1 ou 2)
                raise ValueError()
            
            col = int(input(f"Jogador {player}, escolha a coluna (0, 1 ou 2): ")) # Solicita ao jogador para escolher a coluna
            if col not in [0, 1, 2]:  # Verifica se a entrada da coluna é válida (0, 1 ou 2)
                raise ValueError()
            
            return row, col # Retorna as coordenadas (linha, coluna) escolhidas pelo jogador
        except ValueError: # Caso ocorra um erro (entrada inválida), exibe uma mensagem de erro 
            print("Entrada inválida. Insira um valor correto (0, 1 ou 2) para a linha e a coluna.") #e pede novamente ao jogador para escolher valores corretos.

def play_again():
    while True:
        choice = input("Deseja jogar novamente? (S/N): ").strip().lower()
        if choice == 's':
            return True
        elif choice == 'n':
            return False
        else:
            print("Resposta inválida. Digite 'S' para jogar novamente ou 'N' para sair.")

def main():
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        player = "X"
        computer = "O"
        
        while True:    
            clear_screen()
            print_board(board)
            
            if player == "X":
                row, col = get_player_move(player)
            else:
                print(f"Vez do computador ({computer})")
                sleep(2)
                row, col = computer_move(board)

            if board[row][col] == " ":
                board[row][col] = player

                if check_winner(board, player):
                    clear_screen()
                    print_board(board)
                    print(f"Jogador {player} venceu!" if player == "X" else f"Computador ({computer}) venceu!")
                    break
                elif is_board_full(board):
                    clear_screen()
                    print_board(board)
                    print("Empate!")
                    break
                else:
                    player = "O" if player == "X" else "X"
            else:
                print("Esta posição já está ocupada. Tente novamente.")
                input("Pressione Enter para continuar...")

        if not play_again():
            break

if __name__ == "__main__":
    main()
