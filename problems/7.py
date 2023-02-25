import numpy as np

class PrimeException(Exception):
	pass

def partial_factorize(n):
	for i in range(2, int(np.sqrt(n)) + 1):
		res = n / i
		if res == np.floor(res):
			return i, n/i
	raise PrimeException

def primes():
	i = 2
	while True:
		try:
			partial_factorize(i)
		except PrimeException:
			yield i
		i += 1

def main():
	N = 10001
	n = 0
	for p in primes():
		n += 1
		if n == N:
			return p

if __name__ == "__main__":
	print(main())