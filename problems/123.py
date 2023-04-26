import sys
import numpy as np

def sieve_prime(N):
	marked = np.ones(N, dtype=bool)
	marked[0] = False
	marked[1] = False
	target = int(np.sqrt(N))+1

	for current in range(2, target):
		if not marked[current]:
			continue
		marked[current*current::current] = False

	return marked, np.where(marked)[0]

def main():
	N = 10**10
	K = 1000000
	sieve, primes = sieve_prime(int(np.sqrt(N))+K)

	for n in range(1, int(np.sqrt(N))+K, 2):
		if n-1 >= len(primes):
			break
		p = primes[n-1]
		if (2*p*n) % (p*p) > 10**10:
			return n

	print("Prime Buffer too small")
	sys.exit(1)

if __name__=="__main__":
	print(main())