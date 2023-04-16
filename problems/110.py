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

def main():
	# 1/(n+1) + 1/n*(n+1) = 1/n (k = 1)
	# 1/2n + 1/2n = 1/n (k = n)
	
	# y = nx/(x-n)
	# if x = n+k, y = n(n+k)/k -> k divides n or n+k == k divides n²

	N = 50
	sieve, primes = sieve_prime(N)
	F = 14 # max nb of factors
	K = 5 # max factor value

	numbers = []
	for f in range(3, F+1):
		val = [1] * f
		end = [K] * f

		numbers.append([1, val.copy()])
		for i in range(len(val)):
			numbers[-1][0] *= int(primes[i])**val[i]

		while val != end:
			cursor = len(val) - 1
			while cursor > 0 and val[cursor] == val[cursor-1]:
				cursor -= 1
			val[cursor] += 1
			for c in range(cursor+1, len(val)):
				val[c] = 1

			numbers.append([1, val.copy()])
			for i in range(len(val)):
				f = int(primes[i])**val[i]
				numbers[-1][0] *= f
			assert(numbers[-1][0] > 0)

	numbers.sort(key = lambda x: x[0])

	max, val = 0, 1
	for element in numbers:
		n = element[0]
		counts = {primes[i]:element[1][i] for i in range(len(element[1]))}
		nb_divisors = 1
		for c in counts.values():
			nb_divisors *= 2*c+1
		nb_divisors += 1
		nb_divisors //= 2
		if nb_divisors > 4000000:
			return n

	print("Buffer too small")
	sys.exit(1)

if __name__=="__main__":
	print(main())