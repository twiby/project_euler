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

def rad(n, sieve, primes):
	if n == 1 or n == 0:
		return 1
	factors = prime_factorization(n, sieve, primes)
	unique_factors = set(factors)
	ret = 1
	for f in unique_factors:
		ret *= f
	return ret

def main():
	N = 120000
	sieve, primes = sieve_prime(N)

	all_factors = [prime_factorization(n, sieve, primes) for n in range(N)]

	prime_sieve = np.ones((N, len(primes)), dtype=bool)
	prime_sieve[0,:] = False
	for p in range(len(primes)):
		prime_sieve[primes[p]::primes[p], p] = False
	numbers_without_a_given_prime = {primes[p]: prime_sieve[:, p] for p in range(len(primes))}

	all_rad = np.array([rad(i, sieve, primes) for i in range(N)])

	s = 0

	for c in range(2, N):
		if sieve[c]:
			continue
		factors = all_factors[c]
		unique_factors = set(factors)

		if len(unique_factors) == len(factors):
			continue

		rad_abc = all_rad[c] * all_rad[1:c//2] * all_rad[c-1:c-c//2:-1]
		sel = rad_abc < c

		candidates = 1 + np.where(sel)[0]

		if len(candidates) == 0:
			continue

		sel = np.all([numbers_without_a_given_prime[f][candidates] for f in unique_factors], axis=0)
		s += c*sum(sel)

	return s

if __name__=="__main__":
	print(main())