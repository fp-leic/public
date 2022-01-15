#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 17:44:04 2022

@author: silvio sampaio, jan 2022
"""

DIRECTIONS = ['E', 'N', 'W', 'S']

def start_position(board):
    """
    Compute the start position for a given board.
 
    Parameters
    ----------
    board : List of string
        The defined board.
 
    Returns
    -------
    Tuple
        The initial position in the format (row, col, direction).
    """
    for line in range(len(board)):
        for col in range(len(board[0])):
            if board[line][col] in DIRECTIONS:
                return (line, col, board[line][col])

def move(current_position, board):
    """
    Compute the next valid position based on the current position.

    Parameters
    ----------
    current_position : Tuple
        A tuple (row, col, direction).
    board : List of string
        The defined board.
 
    Returns
    -------
    Tuple
        The next valid position in the format (row, col, direction)
    """
    row, col, direction = current_position
    next_row, next_col, next_direction = current_position
    # hit the cornel
    if board[row][col] == '\\':
        valid_moves = {'E': 'S', 'S': 'E', 'W': 'N', 'N': 'W'}
        next_direction = valid_moves[direction]
    # hit the cornel
    if board[row][col] == '/':
        valid_moves = {'W': 'S', 'S': 'W', 'E': 'N', 'N': 'E'}
        next_direction = valid_moves[direction]

    row_increment = {'E': 0, 'W': 0, 'N': -1, 'S': 1}
    next_row = row + row_increment[next_direction]
    col_increment = {'E': 1, 'W': -1, 'N': 0, 'S': 0}
    next_col = col + col_increment[next_direction]

    return (next_row, next_col, next_direction)

def value_on_board(position, board):
    """
    Gets the value of the board for a given position.
 
    Parameters
    ----------
    position : Tuple
        A tuple (row, col, direction).
    board : List of string
        The defined board.
 
    Returns
    -------
    Char
        The border value at the position [row][col].
    """ 
    line, col, direction = position
    return board[line][col]

def move_ball(board):
    """
    Moves the ball over the board towards to the 'X'.
    
    Parameters
    ----------
    board : List of string
        The defined board.

    Returns
    -------
    List of tuple
        A list of all tuples (row,col) representing the ball movement towards the 'X'.
    """
    # Initialize the first position
    start = start_position(board)
    position = start
    solution = []
    while value_on_board(position, board) != 'X':
        # Save the current position
        solution.append((position[0], position[1]))
        # Move to the next position
        position = move(position, board)
    # Save the final position 'X'
    solution.append((position[0], position[1]))
    return solution

inputs = [
    ["E \\", "/ /", "   ", "\\ X"],
    ["SX", "\\/"],
    ["XS\\", "// ", "\\ /"],
    ["/\\/\\X", " \\/\\W", "\\   /"],
    #
    ["X \\ ", "  \\\\", "   N"],
    ["S ", "\\\\", "//", "\\\\", "//", "\\\\", "//", "X "],
    ["/ X", " E\\", "\\ /"],
    ["X\\  ", " \\\\ ", "  \\W"],
]
for l in inputs:
    print(l, "=>", move_ball(l))