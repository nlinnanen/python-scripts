import numpy as np
import time

# solves a given sudoku board quite efficiently

time = time.start()

og_board = np.array([
						[4, 0, 1, 2, 9, 0, 0, 7, 5],
				    [2, 0, 0, 3, 0, 0, 8, 0, 0],
				    [0, 7, 0, 0, 8, 0, 0, 0, 6],
				    [0, 0, 0, 1, 0, 3, 0, 6, 2],
				    [1, 0, 5, 0, 0, 0, 4, 0, 3],
				    [7, 3, 0, 6, 0, 8, 0, 0, 0],
				    [6, 0, 0, 0, 2, 0, 0, 3, 0],
				    [0, 0, 7, 0, 0, 1, 0, 0, 4],
				    [8, 9, 0, 0, 6, 5, 1, 0, 7]
					])
board = np.array(og_board)
full_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def possible(x, y, n):
	global board
	for i in range(9):
		if board[x][i] == n or board[i][y] == n:
			return False

	sqrX = x//3 * 3
	sqrY = y//3 * 3
	for i in range(3):
		for j in range(3):
			if board[sqrX + i][sqrY + j] == n:
				return False
	return True

def solve():
	global board
	for i in range(9):
		for j in range(9):
			if board[i][j] == 0:
				for k in range(1, 10):
					if possible(i, j, k):
						board[i][j] = k
						solve()
						board[i][j] = 0

				return
	print(board)
	input("More")


solve()

