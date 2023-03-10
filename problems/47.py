import sys
import numpy as np

def prime_factorization_pure(n):
	factors = []

	i = 2
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)

	if n > 1:
		factors.append(n)
	return factors


def prime_factorization(n, sieve, primes):
	if sieve[n]:
		return [n]
	factors = []
	
	p = 0
	i = primes[p]
	while i * i <= n:
		if n % i:
			p += 1
			i = primes[p]
		else:
			n //= i
			factors.append(i)
			if sieve[n]:
				return factors + [n]

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

nb_factors = {}
def four_consecutives(i, sieve, primes):
	for ii in range(4):
		if not i+ii in nb_factors.keys():
			nb_factors[i+ii] = len(set(prime_factorization(i+ii, sieve, primes)))
		if nb_factors[i+ii] < 4:
			return False
	return True

def main():
	N = 200000
	sieve, primes = sieve_prime(N)

	not_sieve = np.logical_not(sieve)
	valid = np.logical_and(not_sieve[:N-3], not_sieve[1:N-2])
	valid = np.logical_and(valid, not_sieve[2:N-1])
	valid = np.logical_and(valid, not_sieve[3:N])
	valid = np.where(valid)[0]

	for i in valid:
		if four_consecutives(i, sieve, primes):
			return i

	print("Buffer too small")
	sys.exit(1)

if __name__=="__main__":
	print(main())
