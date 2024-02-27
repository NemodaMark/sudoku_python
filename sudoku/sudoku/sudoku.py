import random
import msvcrt

def print_board(board):
    for row in board:
        print(" ".join(str(cell) if cell != 0 else "?" for cell in row))

def create_sudoku(size):
    board = [[0 for _ in range(size)] for _ in range(size)]
    solve_sudoku(board, size)
    remove_numbers(board)
    return board

def solve_sudoku(board, size):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    row, col = empty_cell
    numbers = list(range(1, size + 1))
    random.shuffle(numbers)
    for num in numbers:
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board, size):
                return True
            board[row][col] = 0
    return False

def find_empty_cell(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid_move(board, row, col, num):
    # Sor ellenõrzése
    if num in board[row]:
        return False
    # Oszlop ellenõrzése
    if num in [board[i][col] for i in range(len(board))]:
        return False
    # Rács ellenõrzése
    subgrid_size = int(len(board) ** 0.5)
    start_row, start_col = (row // subgrid_size) * subgrid_size, (col // subgrid_size) * subgrid_size
    for i in range(start_row, start_row + subgrid_size):
        for j in range(start_col, start_col + subgrid_size):
            if i < len(board) and j < len(board[0]) and board[i][j] == num:
                return False
    return True

def remove_numbers(board):
    empty_cells = len(board) * len(board) // 2
    while empty_cells > 0:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        if board[row][col] != 0:
            temp = board[row][col]
            board[row][col] = 0
            temp_board = [row[:] for row in board]
            if not solve_sudoku(temp_board, len(board)):
                board[row][col] = temp
                continue
            empty_cells -= 1

def main():
    size = int(input("Adja meg a Sudoku meretet: "))
    sudoku_board = create_sudoku(size)
    print("Sudoku feladvany:")
    print_board(sudoku_board)

    # A felhasznalo a szokoz (SPACEBAR) lenyomasaval mutathatja meg a megoldast
    print("Nyomja meg a SZOKOZT a megoldas megjelenitesere...")
    while True:
        key = msvcrt.getch()
        if key == b' ':
            print("Sudoku megoldasa:")
            solve_sudoku(sudoku_board, size)
            print_board(sudoku_board)
            break

if __name__ == "__main__":
    main()
