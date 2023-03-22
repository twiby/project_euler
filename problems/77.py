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

def nb_ways(n, values):
	if n == 0:
		return 1
	if len(values) == 1:
		return int(n%2 == 0)
	return sum([nb_ways(n-u*values[0], values[1:]) for u in range(n//values[0]+1)])

def main():
	N = 5000
	sieve, primes = sieve_prime(N)
	primes = list(primes)
	primes.reverse()
	primes = np.array(primes)

	n = 10
	while True:
		if nb_ways(n, primes[primes < n]) > N:
			return n
		n += 1

if __name__=="__main__":
	print(main())