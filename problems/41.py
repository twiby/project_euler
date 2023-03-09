import numpy as np

class PrimeException(Exception):
	pass

def partial_factorize(n, sieve):
	for i in sieve:
		if i > np.sqrt(n):
			raise PrimeException
		res = n / i
		if res == np.floor(res):
			return
	raise PrimeException

def is_prime(n, sieve):
	try:
		partial_factorize(n, sieve)
		return False
	except PrimeException:
		return True

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

	return np.where(marked)[0]

def pandigital(n):
	string = str(n)
	s = set([str(i+1) for i in range(len(string))])
	return set(list(string)) == s

def main():
	N = 7654321 ## cannot be with 8 or 9: multiples of 9

	prime_search_limit = int(np.sqrt(N))
	sieve = sieve_prime(prime_search_limit)

	while N > 0:
		while not pandigital(N) and N > 7:
			N -= 1
		if is_prime(N, sieve):
			return N
		N -= 1
	return 0

if __name__=="__main__":
	print(main())