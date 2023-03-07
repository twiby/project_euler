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

	return np.where(marked)[0]
MAX = 12990
sieve = sieve_prime(MAX)

def consecutive_primes(a,b):
	f = lambda n: n**2 + a*n + b
	n = 0
	while f(n) in sieve:
		n += 1
	return n

def main():
	N = 1000

	max_values = (1, 41)
	max = 40
	for b in sieve:
		if b>N:
			break
		for a in sieve-b-1:
			if a>N:
				break
			if not 4+2*a+b in sieve:
				continue
			if consecutive_primes(a,b) > max:
				max = consecutive_primes(a,b)
				max_values = (a,b)

	return max_values[0] * max_values[1]

if __name__=="__main__":
	print(main())

