import numpy as np
from itertools import combinations


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

def is_prime(n, sieve, primes):
	if n < len(sieve):
		return sieve[n]
	max_factor = int(np.sqrt(n))
	for i in primes:
		if i > max_factor:
			break
		elif not n%i:
			return False
	return True

def M(n, d, sieve, primes):
	if d == 1:
		early_exit = int("1"*n)
		if is_prime(early_exit, sieve, primes):
			return n
		base = n-1
	elif d == 0:
		base = n-2
	else:
		base = n-1

	for ret in range(base, 0, -1):
		for c in combinations([i for i in range(n)], n-ret):
			base_digits = [str(d)] * n
			for x in range(10**(n-ret)):
				digits = [c for c in str(x)]
				digits = ["0"]*(n-ret-len(digits)) + digits

				num = base_digits.copy()
				assert(len(c) == len(digits))
				for cc, dd in zip(c, digits):
					num[cc] = dd
				if num[0] == "0":
					continue
				if is_prime(int("".join(num)), sieve, primes):
					return ret
	raise ValueError

def main():
	max_nb_digits = 10
	N = 10**(max_nb_digits + 1)

	sieve, primes = sieve_prime(int(np.sqrt(N)))

	nb_digits = 10
	total = 0
	for d in range(10):
		nb_other = M(nb_digits, d, sieve, primes)

		s = 0
		for c in combinations([i for i in range(nb_digits)], nb_digits-nb_other):
			base_digits = [str(d)] * nb_digits
			for x in range(10**(nb_digits-nb_other)):
				digits = [c for c in str(x)]
				digits = ["0"]*(nb_digits-nb_other-len(digits)) + digits

				num = base_digits.copy()
				assert(len(c) == len(digits))
				for cc, dd in zip(c, digits):
					num[cc] = dd
				if num[0] == "0":
					continue
				if is_prime(int("".join(num)), sieve, primes):
					s += int("".join(num))
		total += s

	return total

if __name__=="__main__":
	print(main())