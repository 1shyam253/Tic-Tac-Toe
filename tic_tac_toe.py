#!/usr/bin/env python3
"""Tic-Tac-Toe - two-player game on a 3x3 board."""
import sys

def show(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3])); 
        if i < 6: print("---------")

def winner(board):
    lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in lines:
        if board[a] == board[b] == board[c] != " ": return board[a]
    return None

def main():
    board, player = [" "] * 9, "X"
    print("Tic-Tac-Toe! Players take turns entering a square number (1-9).")
    while True:
        show(board)
        try: move = int(input(f"Player {player}, choose a square (1-9): ")) - 1
        except (ValueError, EOFError): print("Enter a number 1-9."); continue
        if not 0 <= move <= 8 or board[move] != " ":
            print("That square is taken or invalid, try again."); continue
        board[move] = player
        win = winner(board)
        if win: show(board); print(f"Player {win} wins!"); return
        if " " not in board: show(board); print("It's a draw!"); return
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    main()
