#
# Lecture 14 - Recursive Sudoku Puzzle solver
#
# Fill a 9x9 grid with numbers from 1 to 9 such that
# every row, column and 3x3 subsquare contains only
# one occurence of each number
# https://en.wikipedia.org/wiki/Sudoku
#
# Based on the solution by Thorsten Altenkirch
# https://youtu.be/G_UYXzGuqvM
#
# Pedro Vasconcelos, 2022
#

# An example Sudoku puzzle
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,1,9]]


def possible(y,x,n):
    '''Check if it is valid to place number n at coordinates x,y.'''
    global grid
    # search row y
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    # search column x
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    # seach subsquare of x,y
    x = (x//3)*3
    y = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y+i][x+j] == n:
                return False
    return True

def print_grid():
    '''Print the current state of the grid.'''
    global grid
    for row in grid:
        print(row)   


def solve():
    '''Solve the grid, printing all possible solutions.'''
    global grid
    # list of positions to fill in
    todo = []
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                todo.append((x,y))
    # fill in recursively
    solve_rec(todo)
        

def solve_rec(todo):
    '''Worker function that solves the puzzle recursively.'''
    global grid
    if todo == []:
        # nothing left to do
        # print solution
        print("Solution:")
        print_grid()
    else:
        # first position
        x,y = todo[0]
        # remaining positions
        rest = todo[1:]
        for n in range(1,10):
            if possible(y,x,n):
                grid[y][x] = n
                solve_rec(rest)
                grid[y][x] = 0
