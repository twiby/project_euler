import numpy as np

def pentagonal(n):
	return n*(3*n-1)//2

def main():
	N = 50000000
	pent = np.zeros(N, dtype=bool)
	n = 1
	p = pentagonal(1)
	while p<len(pent):
		pent[p] = True
		n += 1
		p = pentagonal(n)
	pentagonals = np.where(pent)[0]
	
	for sum_idx in range(len(pentagonals)):
		sum = pentagonals[sum_idx]
		for diff in pentagonals[:sum_idx]:
			if pent[(sum+diff)//2] and pent[(sum-diff)//2]:
				return diff
	return 0

if __name__=="__main__":
	print(main())