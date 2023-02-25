import numpy as np

class PrimeException(Exception):
	pass

def partial_factorize(n):
	for i in range(2, int(np.sqrt(n)) + 1):
		res = n / i
		if res == np.floor(res):
			return i, n/i
	raise PrimeException

def factorize(n, top=True):
	try:
		a, b = partial_factorize(n)
		return *factorize(a, False), *factorize(b, False)
	except PrimeException:
		return (int(n),)

def main():
	return np.max(factorize(600851475143))

if __name__ == "__main__":
	print(main())