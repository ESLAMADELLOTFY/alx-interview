#!/usr/bin/python3
"""Module with solution for the N-Queens challenge with backtracking"""
import sys

def print_board(board):
    """Function to print the board with positions of queens."""
    print(board)

def is_safe(board, rank, file):
    """Function to check if placing a queen at (rank, file) is safe."""
    for r in range(rank):
        # Check the same column and diagonals
        if board[r] == file or \
           board[r] - r == file - rank or \
           board[r] + r == file + rank:
            return False
    return True

def solve_nqueens(board, rank, n):
    """Function to solve the N-Queens problem using backtracking."""
    if rank == n:
        print_board(board)
    else:
        for file in range(n):
            if is_safe(board, rank, file):
                board[rank] = file  # Place the queen
                solve_nqueens(board, rank + 1, n)  # Recur to place next queen

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    board = [-1] * n  # Initialize board with -1 (no queens placed)
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    main()
