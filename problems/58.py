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

def is_prime(n, sieve, primes):
	if n < len(sieve):
		return sieve[n]
	
	for i in primes:
		if i*i > n:
			return True
		elif not n % i:
			return False

	m = i % 6

	if m == 1:
		while i * i <= n:
			if n % i:
				i += 4
			else:
				return False
			if n % i:
				i += 2
			else:
				return False
	else:
		while i * i <= n:
			if n % i:
				i += 2
			else:
				return False
			if n % i:
				i += 4
			else:
				return False


	return True

def up_right_diag():
	n = 3
	while True:
		yield n**2
		n += 2 

def up_left_diag():
	n = 3
	for d in up_right_diag():
		yield d - n + 1
		n += 2
def bottom_left_diag():
	n = 3
	for d in up_left_diag():
		yield d - n + 1
		n += 2
def bottom_right_diag():
	n = 3
	for d in bottom_left_diag():
		yield d - n + 1
		n += 2


def main():
	N = 50000
	sieve, primes = sieve_prime(N)

	iter_1 = up_left_diag()
	iter_2 = bottom_left_diag()
	iter_3 = bottom_right_diag()

	n = 0
	count_tot = 1
	count_primes = 0
	condition = True
	while condition:
		count_primes += is_prime(next(iter_1), sieve, primes)
		count_primes += is_prime(next(iter_2), sieve, primes)
		count_primes += is_prime(next(iter_3), sieve, primes)
		count_tot += 4
		condition = (count_primes/count_tot >= 0.1)
		n += 1

	return 2*n+1

if __name__ == "__main__":
	print(main())
