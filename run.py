import random
import colorama
from colorama import Fore, Back, Style


def display_board(board):
    """Prints the board with row numbers and labels."""
if board is None:
    print(f"{Fore.LIGHTBLUE}Game not started yet. Please start the game first.{Style.RESET_ALL}")
else:
    # Print row numbers and labels
    print(f"A   B   C")

    # Print each row with square brackets and colors
    for i, row in enumerate(board, start=1):
        print(f"{i}  ", end="")  # Add row number with a space
    for cell in row:
        if cell == 'X':
            print(f"{Fore.RED}[{cell}]", end="")  # Red for X
        elif cell == 'O':
            print(f"{Fore.BLUE}[{cell}]", end="")  # Blue for O
        else:
            print(f"[ {cell} ]", end="")  # White for empty cells
            print(f"{Style.RESET_ALL}")  # Reset formatting and add newline


def choose_and_update_cell(board, player):
    """Prompts the player to choose a cell and updates the board."""
    while True:
        cell = input(f"Player's turn: ").strip().lower()
        if len(cell) == 2 and cell[0] in 'abc' and cell[1] in '123':
            row = int(cell[1]) - 1
            col = ord(cell[0]) - ord('a')
            if board[row][col] == ' ':
                board[row][col] = player
                return  # Exit the loop after successful placement
            else:
                print("Cell already occupied. Please choose another one.")
        else:
            print(
                f"""{Fore.RED} 
Invalid input. Please enter a letter (A-C) and a number (1-3).
{Style.RESET_ALL}"""
            )


def is_valid_move(board, row, col):
    """Checks if the specified move is valid (cell is empty)."""
    return board[row][col] == ' '


def computer_move(board):
    """Generates a random valid move for the computer."""
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if is_valid_move(board, row, col):
            return row, col


def main():
    """Main game loop."""
    current_player = 'X'  # Start with player X

    print(f"""
                            Welcome to 3 in a Row!

Rules:
- Players take turns placing their mark (X or O) on the board.
- The board is represented by letters (A-C) for columns 
and numbers (1-3) for rows.
- Input your letter then your number (e.g., A1) 
in order to place your mark.
""")
    
    while True:
        display_board(board)  # calling the boardfunction

    # Player's turn
    if current_player == 'X':
        choose_and_update_cell(board, current_player)  # Pass the board

    # Computer's turn
    else:
        print(f"Computer's turn:")
        row, col = computer_move(board)  # Pass the board
        board[row][col] = current_player 