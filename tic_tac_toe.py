import random

board = [" " for i in range(9)]

def show_board():
    print()
    for i in range(0, 9, 3):
        print(" | ".join(
            board[j] if board[j] != " " else str(j + 1)
            for j in range(i, i + 3)
        ))
        if i < 6:
            print("--|---|--")
    print()

def check_winner(player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True

    return False

print("Welcome to Tic Tac Toe!")
print("You are X and Computer is O.")

while True:
    show_board()

    try:
        position = int(input("Enter your position (1-9): ")) - 1
    except ValueError:
        print("Please enter a number!")
        continue

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid position! Try again.")
        continue

    board[position] = "X"

    if check_winner("X"):
        show_board()
        print("Congratulations! You Win!")
        break

    if " " not in board:
        show_board()
        print("Game Draw!")
        break

    computer_position = random.choice(
        [i for i in range(9) if board[i] == " "]
    )

    board[computer_position] = "O"

    print("Computer selected position:", computer_position + 1)

    if check_winner("O"):
        show_board()
        print("Computer Wins! Better luck next time.")
        break

    if " " not in board:
        show_board()
        print("Game Draw!")
        break