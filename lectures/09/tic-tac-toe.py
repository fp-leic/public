#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Oct 2023
@author: nmm
"""

"""
Lecture 09: Lists

Create a 2-player n-dimension tic-tac-toe game through the terminal.
Incomplete: does not detect winning moves.
"""


def empty_board(dimension, empty_symbol):
    """
    Create and return a new board of a given dimension filled with the given empty symbol.
    """
    board = []
    for i in range(dimension):
        # line must be created inside the loop in every iteration, otherwise it will always be the same
        empty_line = dimension * [empty_symbol]
        # our board is a list of lists, so we must concatenate lists of lists
        board = board + [empty_line]
    return board


def play(board, i, j, player, empty_symbol):
    """
    Update the board at (i,j) for the given player, where the empty symbol identifies valid positions. 
    Returns True if a valid play, False otherwise.
    """
    if not (0 <= i < len(board)) or not (0 <= j < len(board)):
        return False
    if board[i][j] != empty_symbol:
        return False
    # this function has side-effects: it only returns a Boolean, but also updates the given board!
    board[i][j] = player
    return True


def player_wins(board, player):
    """
    Determines whether a player has won the game.
    """
    # TODO in a later QP :)
    return False


def pretty_print(board):
    """
    Prints a board in the standard output.
    """
    for line in board:
        for col in line:
            print(col, end=" ")
        print()


def tic_tac_toe(dimension, empty_symbol):
    """
    Plays a game of tic-tac-toe of a given dimension, interacting with the user through the terminal.
    Terminates when a player wins or no more available plays.
    """
    board = empty_board(dimension, empty_symbol)
    pretty_print(board)
    win = False
    plays = 0
    while not win and plays < dimension*dimension:
        # o plays in even turns, x in odd turns
        if plays % 2 == 0:
            player = "o"
        else:
            player = "x"
        print(f"it's {player}'s turn")
        i = int(input("play line: "))
        j = int(input("play column: "))
        # must check results to see if valid play
        good_play = play(board, i, j, player, empty_symbol)
        if good_play:
            pretty_print(board)
            win = player_wins(board, player)
            # only valid plays change the turn
            plays += 1
        else:
            print("bad play")


tic_tac_toe(3, "-")
