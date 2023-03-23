import sys
import numpy as np

def pentagonals(N):
	return np.array([k*(3*k-1)//2 for k in range(-N, N)], dtype = np.int64)

def next_partition(partitions, n, mod, pent, signs):
	k_min = int(-(np.sqrt(24*n+1) - 1)/6) + len(pent)//2
	k_max = int((np.sqrt(24*n+1)+1)/6)+1 + len(pent)//2

	s = np.sum(signs[k_min: k_max] * partitions[n - pent[k_min: k_max]])
	return s % mod

def main():
	N = 1000000
	
	MAX_RECURRENCE = 500
	pent = pentagonals(MAX_RECURRENCE)
	signs = np.array([(-1)**(k+1) for k in range(2*MAX_RECURRENCE)])

	MAX_NB_TERMS = 100000
	p = np.array([0 for _ in range(MAX_NB_TERMS)])
	p[0] = 1
	p[1] = 1

	n = 1
	while p[n]:
		n += 1
		p[n] = next_partition(p, n, N, pent, signs)
	return n

if __name__=="__main__":
	print(main())