import numpy as np
import random
from collections import defaultdict


""" 

2048

its the classic game of 2048 played in the terminal.

"""

def restart(grid):
    grid = np.zeros((4,4))
    grid = new_tile(grid)
    grid = new_tile(grid)
    return grid

def new_tile(grid):
    empty = get_empty_cells(grid)
    if empty:
        rand_empty = empty[random.randint(0, len(empty)-1)]
        grid[rand_empty[0]][rand_empty[1]] = 2 if random.randint(1, 10)<9 else 4

    return grid


def get_empty_cells(grid):
    empties = np.where(grid == 0)
    return list(zip(empties[0], empties[1]))

def game_over(grid):
    empties = get_empty_cells(grid)
    for i in range(4):
        rot = np.rot90(grid, i)
        for j in range(4):
            for k in range(1, 4):
                if rot[j][k] == rot[j][k-1] or empties != []:
                    return False
    return True

def move(grid, move_num, score):

    if str(move_num) not in ('0', '1', '2', '3', '4'):
        print("Invalid input: {}".format(move_num))
        return (grid, score, False)

    moved = False # tracker to see if something has moved

    # IMPORTANT: rotates the grid so that the moving works by shifting everything to the left
    grid = np.rot90(grid, int(move_num))

    for i_row, row in enumerate(grid):      # looping thourgh the grid
        zeros = []          # list for the zeros in the row
        merged = []         # soon to be list of bools. True if the corresponding index has merged
                            # this is how we avoid double merging

        for i_col, cell in enumerate(row):
            merged.append(False)
            if cell != 0: # we don't move zeros

                merge = -1 # holds the index with which to merge with on the row
                for k in range(i_col): # compare each cell on the row to the current cell


                    # if the same value is found and the we haven't yet found an 'earlier' mergable tile on the row
                    # and the tile with the same value is not merged tile itself, we have found an index to merge with
                    if row[k] == cell and merge == -1 and not merged[k]:
                        merge = k


                    # but if we find an unempty sell with the wrong value,
                    elif row[k] != 0 and row[k] != cell:
                        merge = -1

                if merge != -1:
                    grid[i_row][merge] = 2*cell
                    merged[merge] = True
                    score += 2*cell
                    grid[i_row][i_col] = 0
                    zeros.append(i_col)
                    moved = True

                elif zeros != []: #zeros not empty because otherwise no space
                    grid[i_row][min(zeros)] = cell
                    zeros.remove(min(zeros))
                    grid[i_row][i_col] = 0
                    zeros.append(i_col)
                    moved = True


            elif cell == 0:
                zeros.append(i_col)

    grid = np.rot90(grid, -int(move_num))
    if moved:
        grid = new_tile(grid)

    return (grid, score, moved)

def main():
  print("2048")
  print("----")
  print("up: 1, right 2: down: 3, left 4")
  grid = np.zeros((4,4))
  grid = restart(grid)
  score = 0
  while(not game_over(grid)):
      print(grid)
      inpt = input("Move: ").strip()
      print(inpt)
      if inpt:
        grid, score, valid = move(grid, inpt, score)
      else:
        print("You must input something!")


if __name__ == '__main__':
    main()