import sys
import numpy as np

def permuts_that_are_cubes(lst, tree, ret = 0, n = 0):
	for n in lst:
		tree = tree[0][n]
	return tree[1]

def cubes_permuts(n, tree):
	input = [int(c) for c in str(n)]
	input.sort()
	return permuts_that_are_cubes(input, tree)

def main():
	N = 1000000000000
	

	cubes_lst = []
	cubes_tree = [[None for _ in range(10)], 0]

	i = int(np.cbrt(100)) + 1
	c = i ** 3
	while c < N:
		cubes_lst.append(c)

		input = [int(ch) for ch in str(c)]
		input.sort()

		tree = cubes_tree
		for n in input:
			if tree[0][n] is None:
				tree[0][n] = [[None for _ in range(10)], 0]
			tree = tree[0][n]
		tree[1] += 1

		i += 1
		c = i**3

	for n in cubes_lst:
		if cubes_permuts(n, cubes_tree) == 5:
			return n

	print("Buffer too small")
	sys.exit(1)

if __name__ == "__main__":
	print(main())
