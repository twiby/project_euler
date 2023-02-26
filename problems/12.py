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

def factor_count(factors):
	ret = {}
	for f in factors:
		if f in ret.keys():
			ret[f] += 1
		else:
			ret[f] = 1
	return ret

def nb_divisors(factor_count):
	prod = 1
	for k,v in factor_count.items():
		prod *= v+1
	return prod

def nth_triangular(n):
	return n*(n+1)//2

def main():
	N = 500
	factors = list(factorize(2))
	i = 2
	while True:
		next_factors = list(factorize(i+1))
		curr_factors = factors + next_factors
		curr_count = factor_count(curr_factors)
		curr_count[2] -= 1

		if nb_divisors(curr_count) > N:
			return nth_triangular(i)
		factors = next_factors
		i += 1

if __name__ == "__main__":
	print(main())