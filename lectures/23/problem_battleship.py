#
# Lecture 23 - Battleship mini-game
#
# Pedro Vasconcelos, 2023

import random
from typing import List, Tuple, Dict

Loc = Tuple[int,int]   # row, col


def place_ship(size: int, grid: Dict[Loc,int]) -> None:
    """Place a ship of given size on a grid; modifier function."""
    while True: # repeat until the ship fits
        # choose orientation
        orient = random.randint(0,1)
        # choose start location
        x = random.randint(1,10)
        y = random.randint(1,10)
        if orient:
            locs = [(x+k,y) for k in range(size) if x+k<=10 and (x+k,y) not in grid]
        else:
            locs = [(x,y+k) for k in range(size) if y+k<=10 and (x,y+k) not in grid]
        if len(locs) == size:
            break
    for loc in locs:
        grid[loc] = size
       
    
def place_ships(ships: List[int]) -> Dict[Loc,int]:
    """Place a list of ships into an empty grid."""
    grid : Dict[Loc,int] = dict()
    for size in ships:
        place_ship(size, grid)
    return grid

def print_grid(grid: Dict[Loc,int]) -> None:
    """Print a grid (for debugging only)."""
    for row in range(1,11):
        for col in range(1,11):
            if (row,col) in grid:
                print(grid[row,col], end='')
            else:
                print('.', end='')
        print()


def print_shots(shots: Dict[Loc,str]) -> None:
    """Print the shots already taken by the player."""
    print(' ', end='')
    for col in range(1,11):
        print(col, end='')
    print()
    for row in range(1,11):
        print(chr(ord('A')+row-1), end='')
        for col in range(1,11):
            if (row,col) in shots:
                print(shots[row,col], end='')
            else:
                print('.', end='')
        print()

        
        
def get_location(txt: str) -> Loc:
    """Convert a text into a location."""
    if len(txt)<2:
        raise ValueError('invalid position')
    txt = txt.upper()
    row = txt[0]
    col = int(txt[1:])
    if 'A' <= row and row <= 'J' and 1 <= col and col<= 10:
        return (ord(row)-ord('A')+1,col)
    else:
        raise ValueError(f'iliteral for int() nvalid position: {txt}')

def read_loc() -> Loc:
    """Try to read a line and convert to a location."""
    repeat = True
    while repeat:
        try:
            loc = get_location(input("Location? "))
            repeat = False
        except ValueError as err:
            print(err)
        except EOFError:
            print()
    return loc
    
def battleship():
    """Play a game of battleship."""
    ships = [2, 3, 4, 5]
    grid = place_ships(ships)
    shots = dict()
    while len(grid) > 0:
        print_shots(shots)
        print("Enemy ships: ", ships)
        loc = read_loc()          
        if loc in grid:
            print("Hit!")
            shots[loc] = 'X'
            size = grid[loc]
            del grid[loc]
            if size not in grid.values():
                print(f'Sunk ship of size {size}!')
                ships.remove(size)
        elif loc in shots:
            print("Already shot!")
        else:
            print("Miss...")
            shots[loc] = '!'
    print("End of game")


if __name__ == "__main__":
    battleship()
