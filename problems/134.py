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
	N = 1000004
	sieve, primes = sieve_prime(N)
	primes = primes[2:]

	multiplicants = {i: {} for i in range(1, 10)}
	for i in range(1, 10):
		for j in range(1, 10):
			k = 0
			while k*j%10 != i:
				k += 1
				if k == 10:
					break
			if k == 10:
				continue
			multiplicants[i][j] = k

	s = 0
	for p_idx in range(len(primes) - 1):
		p1 = primes[p_idx]
		p2 = primes[p_idx + 1]
		lever = p2 % 10

		p1_digits = [int(c) for c in str(p1)]
		p1_digits.reverse()

		curr = 0
		for i in range(len(p1_digits)):
			target = (p1_digits[i] - (curr//(10**i))%10)%10
			if target == 0:
				continue
			x = multiplicants[target][lever]

			curr += (10**i) * p2 * x
		s += curr

	return s

if __name__=="__main__":
	print(main())