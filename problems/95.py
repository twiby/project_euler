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
	N = 1000000
	K = N
	sieve, primes = sieve_prime(K)
	sum_divisors = np.ones(K, dtype=np.int64)

	multiplier = np.ones(K, dtype=np.int64)
	for p in primes:
		val = 1
		length = (N//p+1 if N%p else N//p) - 1
		while val < N:
			multiplier[val-1:length:val] = (val*p*p-1)
			val *= p
		multiplier[:length] //= p-1
		sum_divisors[p::p] *= multiplier[:length]
		multiplier[:length] = 1

	minus = np.array([n for n in range(N)])
	sum_divisors -= minus

	max_chain_len = 0
	ret = 0
	visited = np.zeros(K, dtype=bool)
	for n in range(2, N):
		if visited[n] or sieve[n]:
			continue

		chain = set()
		chain.add(n)
		visited[n] = True
		while not sum_divisors[n] in chain:
			n = sum_divisors[n]
			if n > N or visited[n]:
				n = 0
				break
			chain.add(n)
			visited[n] = True

		if n > 0:
			chain_image = set([sum_divisors[c] for c in chain])
			while chain_image != chain:
				chain = chain_image
				chain_image = set([sum_divisors[c] for c in chain])

			if len(chain) > max_chain_len:
				max_chain_len = len(chain)
				ret = min(chain)
	return ret

if __name__=="__main__":
	print(main())