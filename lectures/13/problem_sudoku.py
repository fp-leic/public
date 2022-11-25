#
# Lecture 13 - Recursive Sudoku Puzzle solver
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
example_grid = [[5,3,0,0,7,0,0,0,0],
                [6,0,0,1,9,5,0,0,0],
                [0,9,8,0,0,0,0,6,0],
                [8,0,0,0,6,0,0,0,3],
                [4,0,0,8,0,3,0,0,1],
                [7,0,0,0,2,0,0,0,6],
                [0,6,0,0,0,0,2,8,0],
                [0,0,0,4,1,9,0,0,5],
                [0,0,0,0,8,0,0,1,9]]


def check_possible(grid,number,row,col):
    '''Check if it is valid to place number at coordinates row,col.'''
    # search row 
    for i in range(0,9):
        if grid[row][i] == number:
            return False
    # search column
    for i in range(0,9):
        if grid[i][col] == number:
            return False
    # seach subsquare of x,y
    # origin of the subsquare
    r = (row//3)*3
    c = (col//3)*3
    # iterate over 3*3 subsquare
    for i in range(0,3):
        for j in range(0,3):
            if grid[r+i][c+j] == number:
                return False
    # all other cases: possible
    return True

def print_grid(grid):
    '''Print the current state of the grid.'''
    print("Solution:")
    for row in grid:
        print(row)   
    print(40*'-')


def solve(grid):
    '''Solve the grid, printing all possible solutions.'''
    # list of positions to fill in
    zeros = []
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                zeros.append((row,col))
    # fill in recursively
    solve_rec(grid,zeros)
        

def solve_rec(grid, zeros):
    '''Worker function that solves the puzzle recursively.'''
    if len(zeros) == 0:
        # finished; just print the solution
        print_grid(grid)
    else:
        # first zero position
        (row,col) = zeros[0]
        # remaining positions
        rest = zeros[1:]
        for number in range(1,10):
            # check if we can place number at row,col 
            if check_possible(grid,number,row,col):
                # place number and recursively continue
                grid[row][col] = number
                solve_rec(grid,rest)
                # undo the placement to try other alternatives
                grid[row][col] = 0


# ---------------------------------------------
# Solve the example grid
solve(example_grid)
