import numpy as np

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

def repeating_cycle(n):
	if n == 2 or n == 5:
		return 0
	exp = 1
	base = 10

	while base % n > 1:
		base *= 10
		exp += 1
	return exp

def main():
	N = 1000
	sieve = sieve_prime(N)
	return sieve[np.argmax([repeating_cycle(n) for n in sieve])]

if __name__=="__main__":
	print(main())