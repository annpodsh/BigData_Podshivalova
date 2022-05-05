"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

>>> line1 = [['o', 'x', 'o'],['x', 'o', 'o'],['o', 'x', '0']]
>>> print(tic_tac_toe_checker(line1))
o wins!
>>> line2 = [['x', 'o', 'x'],['o', 'x', 'o'],['o', 'x', 'o']]
>>> print(tic_tac_toe_checker(line2))
unfinished!
>>> line3 = [['0', '-', 'o'],['-', 'x', 'o'],['x', 'o', '-']]
>>> print(tic_tac_toe_checker(line3))
draw!
"""
from typing import List
import itertools
import numpy as np


a = [['x', 'o', 'x'],
     ['x', 'o', 'x'],
     ['o', 'x', 'x']]


def tic_tac_toe_checker(board: List[List]) -> str:
    unfinished = False
    for i in enumerate(board):  # (0, [x,x,x])
        # checking for unfinished game
        if '-' in i[1]:
            unfinished = True
        # horizontal win check
        if len(set(i[1])) == 1 and i[1][0] != '-':
            return f"{i[1][0]} wins"
        # vertical win check
        elif board[0][i[0]] == board[1][i[0]] == board[2][i[0]] != '-':
            return f"{i[1][i[0]]} wins"
        # checking for a diagonal win
        if board[0][0] == board[1][1] == board[2][2] \
                or board[2][0] == board[1][1] == board[0][2]:
            return f"{i[1][1]} wins"
    if unfinished:
        return "unfinished"
    else:
        return "draw"


if __name__ == '__main__':
    import doctest
