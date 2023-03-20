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
	N = 10000000
	sieve, primes = sieve_prime(N)

	sqrt_N = int(np.sqrt(N))
	search_radius = 1000

	sel = np.where(np.logical_and(primes > sqrt_N-search_radius, primes < sqrt_N+search_radius))[0]
	primes_reduced = primes[sel]

	min, min_value = 100,0
	for i1 in range(len(primes_reduced)):
		vals = primes_reduced[i1] * primes_reduced
		totients = (primes_reduced[i1] - 1) * (primes_reduced - 1)
		n_totients = vals / totients
		indices = n_totients.argsort()

		for n in indices:
			if n_totients[n] > min:
				break
			if vals[n] >= N:
				continue
			s1 = np.array([c for c in str(vals[n])])
			s2 = np.array([c for c in str(totients[n])])
			if len(s1) != len(s2):
				continue

			s1.sort()
			s2.sort()
			if (s1 == s2).all():
				min = n_totients[n]
				min_value = vals[n]
	return min_value

if __name__ == "__main__":
	print(main())
