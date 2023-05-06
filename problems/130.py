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

def A(n):
	if n % 2 == 0 or n % 5 == 0:
		raise ValueError

	k = 1
	m = 1
	while m != 0:
		m = (10*m + 1) % n
		k += 1
	return k

def main():
	N = 20000
	sieve, primes = sieve_prime(N)

	lst = []
	for n in range(1, N//10):
		for last_digit in [1,3,7,9]:
			val = 10*n + last_digit
			if sieve[val]:
				continue
			a = A(val)
			if (val-1) % a == 0:
				lst.append(val)
				if len(lst) == 25:
					return sum(lst)

	print("search space too small")
	sys.exit(1)

if __name__=="__main__":
	print(main())
