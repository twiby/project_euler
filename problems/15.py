import numpy as np

def nb_paths(N, x, y):
	'''costly recursive'''
	if x==0 or y==0:
		return 1
	else:
		return nb_paths(N,x-1,y) + nb_paths(N,x,y-1)

def main():
	N = 20

	grid = np.ones((N+1,N+1), dtype=int)

	for x in range(1,N+1):
		for y in range(1,N+1):
			grid[x,y] = grid[x-1,y] + grid[x,y-1]

	return grid[N, N]

if __name__ == "__main__":
	print(main())