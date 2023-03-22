import numpy as np

def main():
	N = 100

	table = np.zeros((N+1,N+1), dtype=np.int64)
	table[0,:] = 1
	table[1,:] = 1

	for i in range(2, N+1):
		table[i,1] = 1
		for j in range(2, i):
			table[i,j] = table[i::-j, j-1].sum()
		table[i, i:] = table [i, i-1] + 1
	return table[N, N-1]

if __name__=="__main__":
	print(main())