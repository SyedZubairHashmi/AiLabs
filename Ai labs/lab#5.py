def is_safe(board, row, col, n):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, n):
    # If all queens are placed, return true
    if col >= n:
        return True 

    # Try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_nqueens_util(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then backtrack and remove the queen from board[i][col]
            board[i][col] = 0

    # If the queen cannot be placed in any row in this column col, return false
    return False

def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]
    if not solve_nqueens_util(board, 0, n):
        print("Solution does not exist")
        return False
    print_solution(board)
    return True

def print_solution(board):
    for row in board:
        print(" ".join('Q' if x == 1 else '.' for x in row))


n = 4
solve_nqueens(n)
