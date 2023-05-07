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

def main():
	### N^3 + N^2*p = k^3

	### N^2*(N+p) = k^3

	### p = (k^3 - n^3)/n^2

	### a^2 - b^2 = (a+b)(a-b)

	### ()

	N = 10000
	sieve, primes = sieve_prime(N)

	cubes = [n*n*n for n in range(N)]

	last_good_n = 1
	last_good_k = 2


	nb = 0
	for p in primes:
		# print(p)
		k = last_good_k
		n = last_good_n

		while k < N and n < N:
			candidate = (cubes[k] - cubes[n])/n/n
			if candidate < p:
				k += 1
			elif candidate > p:
				n += 1
			elif (cubes[k] - cubes[n]) % (n*n) == 0:
				print("GOOD",p, n, k, k-n, np.sqrt(k-n))
				last_good_n = n
				last_good_k = k
				nb += 1
				break
			else:
				k += 1


	return nb

if __name__=="__main__":
	print(main())