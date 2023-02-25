import numpy as np

class PrimeException(Exception):
	pass

def partial_factorize(n):
	for i in range(2, int(np.sqrt(n)) + 1):
		res = n / i
		if res == np.floor(res):
			return i, n/i
	raise PrimeException

def is_prime(n):
	for i in range(2, int(np.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

def primes(max):
	yield 2
	yield 3
	for i in range(1, max):
		i1 = 6*i - 1
		i2 = 6*i + 1

		if i1 > max:
			return
		elif is_prime(i1):
			yield i1


		if i2 > max:
			return
		elif is_prime(i2):
			yield i2


def main():
	N = 2000000
	return np.sum([p for p in primes(N)])

if __name__ == "__main__":
	print(main())