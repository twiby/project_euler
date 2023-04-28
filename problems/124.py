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

def first_prime_factor(n, sieve, primes):
	assert(not sieve[n])
	
	p = 0
	i = primes[p]
	while i * i <= n:
		if n % i:
			p += 1
			i = primes[p]
		else:
			return i

def main():
	N = 100000
	sieve, primes = sieve_prime(N+1)

	rad = np.zeros(N+1, dtype=np.uint64)
	rad[1] = 1

	rad[primes] = primes
	for n in range(2, N+1):
		if rad[n]:
			continue
		p = first_prime_factor(n, sieve, primes)
		f = n//p
		if not f%p:
			rad[n] = rad[f]
		else:
			rad[n] = rad[f] * p

	pairs = np.array([[n, rad[n]] for n in range(N+1)], dtype=np.uint64)
	pairs = pairs.transpose()

	sorting = np.lexsort(pairs)
	return sorting[10000]

if __name__=="__main__":
	print(main())