import sys
import numpy as np

def triangular(n):
	return n*(n+1)//2
def pentagonal(n):
	return n*(3*n-1)//2
def hexagonal(n):
	return n*(2*n-1)

def main():
	N = 10000000000

	pent = np.zeros(N, dtype=bool)
	n = 1
	p = pentagonal(1)
	while p<len(pent):
		pent[p] = True
		n += 1
		p = pentagonal(n)

	hex = np.zeros(N, dtype=bool)
	n = 1
	h = hexagonal(1)
	while h<len(hex):
		hex[h] = True
		n += 1
		h = hexagonal(n)

	t = 0
	for i in range(N):
		t += i
		try:
			if pent[t] and hex[t]:
				if t > 40755:
					return t
		except IndexError:
			print("Buffer not big enough")
			sys.exit(1)
	return 0

if __name__=="__main__":
	print(main())