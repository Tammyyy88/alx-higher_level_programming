#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]"""
    # Check for queens in the same column
    for i in range(row):
        if board[i][col]:
            return False

    # Check for queens in the upper diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check for queens in the lower diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(N):
    """Solve the N-Queens problem"""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def backtrack(row):
        """Backtracking function to find solutions"""
        nonlocal solutions
        if row == N:
            solution = [
                [i, j]
                for i in range(N)
                for j in range(N)
                if board[i][j]
            ]
            solutions.append(solution)
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    backtrack(0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
