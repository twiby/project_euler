import numpy as np
from multiprocessing import Pool
from multiprocessing import cpu_count
from multiprocessing import set_start_method

def solve(grid, first = True):
	if (grid[:,:] > 0).all():
		return True
	zeros = np.where(grid[:,:] == 0)
	zeros = [(x,y) for x,y in zip(zeros[0], zeros[1])]
	assert(_solve(grid, zeros))
	top_3 = grid[0, :3]
	return top_3[0]*100 + top_3[1]*10 + top_3[2]

def _solve(grid, zeros):
	if zeros == []:
		return True

	new = zeros[0]
	square = (3*(new[0]//3), 3*(new[1]//3))

	possible_values = np.array([True for _ in range(10)])
	possible_values[grid[:, new[1]]] = False
	possible_values[grid[new[0], :]] = False
	possible_values[grid[square[0], square[1]:square[1]+3]] = False
	possible_values[grid[square[0]+1, square[1]:square[1]+3]] = False
	possible_values[grid[square[0]+2, square[1]:square[1]+3]] = False
	possible_values = np.where(possible_values[:] == True)[0]

	if len(possible_values) == 0:
		return False

	for val in possible_values:
		grid[new] = val
		if _solve(grid, zeros[1:]):
			return True
	grid[new] = 0
	return False

def main():
	grids = []
	with open("./data/p096_sudoku.txt","r") as f:
		while True:
			try:
				next(f)
			except StopIteration:
				break
			new_grid = np.zeros((9,9), dtype=np.int64)
			for l in range(9):
				line = next(f)
				if line[-1] == "\n":
					line = line[:-1]
				new_grid[l,:] = [int(c) for c in line]
			grids.append(new_grid.copy())

	set_start_method('fork')
	pool = Pool(cpu_count())
	results = pool.map(solve, grids)

	return sum(results)

if __name__=="__main__":
	print(main())