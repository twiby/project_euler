import sys
import numpy as np
from operator import mul

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

def first_prime(n, sieve, primes):
	p = 0
	i = primes[p]
	while i * i <= n:
		if n % i:
			p += 1
			i = primes[p]
		else:
			n //= i
			return i, n

def compute_divisors(n, sieve, primes, divisors):
	assert(not sieve[n])
	p, q = first_prime(n, sieve, primes)
	s = set()
	for d in divisors[q]:
		s.add(d)
		s.add(p*d)
	s.add(p)
	s.add(q)
	divisors[n] = s

def all_product_sums(n, div_trunc, square_roots, sum = 0, length = 0):
	for i in range(len(div_trunc)):
		d = div_trunc[i]
		if d > square_roots[n]:
			return
		elif n%d:
			continue

		yield (sum + d + n//d, length + 2)
		yield from all_product_sums(n//d, div_trunc[i:], square_roots, sum = sum+d, length = length + 1)

def main():
	N = 12201
	sieve, primes = sieve_prime(N)
	square_roots = [np.sqrt(n) for n in range(N)]

	minimial_product_sum = np.zeros(N, dtype = np.int64)
	minimial_product_sum[0] = 1
	minimial_product_sum[1] = 1
	minimial_product_sum[2] = 4

	divisors = [[] for _ in range(N)]
	multiplications_new = [[] for _ in range(N)]
	multiplications_new[4] = [[2,2]]
	multiplications = []
	for n in range(5, N):
		if sieve[n]:
			continue
		max_div = int(np.sqrt(n))

		compute_divisors(n, sieve, primes, divisors)
		div = list(divisors[n])
		div.sort()
		i = 0
		while i < len(div) and div[i] <= max_div:
			i += 1
		div_trunc = div[:i]

		product_sums = [m for m in all_product_sums(n, div_trunc, square_roots)]
		for s, l in product_sums:
			product_sum = (n - s) + l
			if minimial_product_sum[product_sum] == 0:
				minimial_product_sum[product_sum] = n

	if len(np.where(minimial_product_sum[:12001] == 0)[0]) > 0:
		print("Buffer too small")
		sys.exit(1)

	return sum(set(minimial_product_sum[:12001])) - 1


if __name__=="__main__":
	print(main())