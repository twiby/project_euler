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

def left_prune(n):
	nb_digits = len(str(n))
	for i in range(1,nb_digits):
		yield n % (10**i)
def right_prune(n):
	while n > 10:
		n //= 10
		yield n
def prunes(n):
	yield from left_prune(n)
	yield from right_prune(n)

def main():
	N = 1000000
	sieve = set(sieve_prime(N))

	sum = 0
	for n in sieve:
		if n<10:
			continue

		all_in = True
		for p in prunes(n):
			if not p in sieve:
				all_in = False
				break
		if all_in:
			sum += n
	return sum

if __name__=="__main__":
	print(main())
