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

def divisors_gen(factors, prior = 1):
	yield prior
	if len(factors) == 1:
		yield factors[0]*prior
	else:
		for i in range(len(factors)):
			yield from divisors_gen(factors[i+1:], prior = prior * factors[i])
def divisors(n):
	s = set(divisors_gen(factorize(n)))
	s.remove(n)
	return s

def sum_divisors(n):
	return sum(divisors(n))

def main():
	N = 10000
	D = [sum_divisors(n) for n in range(N)]


	sum_amicable = 0
	for n in range(2, N):
		if D[n] != n and D[n] < N and D[D[n]] == n:
			sum_amicable += n

	return sum_amicable

if __name__ == "__main__":
	print(main())
