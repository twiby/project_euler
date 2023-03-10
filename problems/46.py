import sys
import numpy as np

def sieve_prime(N):
	marked = np.ones(N, dtype=bool)
	marked[0] = False
	marked[1] = False
	target = np.sqrt(N)

	current = 1
	while current < target:
		current += 1
		while not marked[current]:
			current += 1

		cursor = current * current
		while cursor < N:
			marked[cursor] = False
			cursor += current

	return marked, np.where(marked)[0]

def main():
	N = 10000
	sieve, primes = sieve_prime(N)
	
	for i in range(3,N,2):
		if sieve[i]:
			continue
		squre_found = False
		for r in range(1, int(np.sqrt(i/2))+1):
			if sieve[i - 2*r*r]:
				squre_found = True
				break
		if not squre_found:
			return i
	print("Prime buffer not big enough")
	sys.exit(1)

if __name__=="__main__":
	print(main())