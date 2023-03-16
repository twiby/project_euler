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

	sieve, primes = sieve_prime(20)

	i = 0
	prod = 1
	while primes[i]*prod < N:
		prod *= primes[i]
		i += 1

	return prod

if __name__ == "__main__":
	print(main())
