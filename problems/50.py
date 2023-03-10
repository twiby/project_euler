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
	N = 1000000

	sieve, primes = sieve_prime(N)

	max_l = 1
	while sum(primes[:max_l]) < N:
		max_l += 1

	for l in range(max_l, 1, -1):
		for i in range(max_l-l+1):
			s = sum(primes[i:i+l])
			if s >= N:
				break
			if sieve[s]:
				return s

	sys.exit(1)

if __name__ == "__main__":
	print(main())