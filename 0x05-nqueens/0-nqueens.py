### nqueens.py
```python
#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens_util(board, col):
    if col >= len(board):
        return [[(i, row.index(1)) for i, row in enumerate(board)]]
    solutions = []
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            for solution in solve_nqueens_util(board, col + 1):
                solutions.append(solution)
            board[i][col] = 0
    return solutions

def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]
    return solve_nqueens_util(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)
