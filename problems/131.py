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

def is_square(n):
	candidate = int(round(np.sqrt(n)))
	if candidate*candidate == n:
		return True
	return False

def main():
	N = 1000000
	sieve, primes = sieve_prime(N)

	squares = set([n*n for n in range(N)])
	max_square = max(squares)

	nb = 0
	last_good_sqrt_k_prime = 1
	for p in primes[2:]:
		sqrt_k_prime = int(np.sqrt(p/3))
		k_prime = sqrt_k_prime * sqrt_k_prime
		d = 9*(k_prime**2) - 4*k_prime*(3*k_prime-p)
		if d > max_square:
			print("not enough squares")
			sys.exit(1)
		if not d in squares:
			continue
		n = (-k_prime*round(np.sqrt(d)) - 3*(k_prime**2))
		if n % (2*(3*k_prime - p)):
			continue
		nb += 1

	return nb

if __name__=="__main__":
	print(main())
