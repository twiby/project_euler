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
	N = 50000000

	sieve, primes = sieve_prime(int(np.sqrt(N))+1)

	primes_squared = primes * primes
	primes_cubed = primes_squared * primes
	primes_fourth = primes_cubed * primes
	primes_squared = primes_squared[primes_squared<N]
	primes_cubed = primes_cubed[primes_cubed<N]
	primes_fourth = primes_fourth[primes_fourth<N]

	expressable = np.zeros(N, dtype = bool)

	for p1 in primes_cubed:
		sq_p_cb = primes_squared + p1
		for p2 in primes_fourth:
			current = sq_p_cb + p2
			current = current[current < N]
			expressable[current] = True

	return np.sum(expressable)

if __name__=="__main__":
	print(main())
