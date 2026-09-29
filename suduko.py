def is_valid_sudoku(board):
    # Check rows
    for row in board:
        numbers = [num for num in row if num != 0]
        if len(numbers) != len(set(numbers)):
            return False

    # Check columns
    for col in range(9):
        numbers = []
        for row in range(9):
            if board[row][col] != 0:
                numbers.append(board[row][col])

        if len(numbers) != len(set(numbers)):
            return False

    # Check 3x3 boxes
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            numbers = []

            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] != 0:
                        numbers.append(board[i][j])

            if len(numbers) != len(set(numbers)):
                return False

    return True


def main():
    print("========== SUDOKU VALIDATOR ==========")

    board = []

    print("\nEnter Sudoku row by row.")
    print("Use 0 for empty cells.")

    for i in range(9):
        while True:
            row = list(map(int, input(f"Row {i + 1}: ").split()))

            if len(row) == 9 and all(0 <= num <= 9 for num in row):
                board.append(row)
                break
            else:
                print("Enter exactly 9 numbers between 0 and 9.")

    if is_valid_sudoku(board):
        print("\nResult: Valid Sudoku")
    else:
        print("\nResult: Invalid Sudoku")


if __name__ == "__main__":
    main()