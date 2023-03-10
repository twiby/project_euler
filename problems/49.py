import sys
import itertools
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

	return marked, np.where(marked)[0]

def num(v):
	return int("".join([str(c) for c in v]))

def permut(values):
	yield from itertools.permutations(values)

def sequences_of_three(values):
	yield from itertools.combinations(values, 3)

def main():
	N = 10000
	sieve, primes = sieve_prime(N)

	sequences = set()
	for i in primes:
		if i < 1000:
			continue
		numbers = [int(c) for c in str(i)]

		prime_permut = set()
		for p in permut(numbers):
			if sieve[num(p)]:
				prime_permut.add(num(p))


		if len(prime_permut) < 3:
			continue

		for seq in sequences_of_three(prime_permut):
			seq_l = list(seq)
			seq_l.sort()
			if seq_l[2]-seq_l[1]==seq_l[1]-seq_l[0]:
				sequences.add(seq)

	for s in sequences:
		string = "".join([str(ss) for ss in s])
		if len(string) == 12 and s[0] != 1487:
			return string
	sys.exit(1)

if __name__ == "__main__":
	print(main())
