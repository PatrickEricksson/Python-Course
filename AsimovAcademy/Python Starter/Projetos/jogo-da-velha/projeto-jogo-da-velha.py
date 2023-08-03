def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Verificar linhas, colunas e diagonais
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"Jogador {current_player}, escolha a linha (0, 1, 2): "))
        col = int(input(f"Jogador {current_player}, escolha a coluna (0, 1, 2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Jogador {current_player} venceu!")
                break
            elif is_board_full(board):
                print_board(board)
                print("Empate!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Essa posição já está ocupada. Tente novamente.")

if __name__ == "__main__":
    main()
