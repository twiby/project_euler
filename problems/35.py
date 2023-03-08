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

def num(digits):
	return int("".join([str(i) for i in digits]))
def digit_rotations(n):
	digits = [int(c) for c in str(n)]
	for d in range(len(digits)):
		yield digits[-d:] + digits[:-d]
	return


def main():
	N = 1000000
	sieve = set(sieve_prime(N))

	count = 0
	for p in sieve:
		all_in = True
		for n in digit_rotations(p):
			if not num(n) in sieve:
				all_in = False
				break
		if all_in:
			count += 1
	
	return count

if __name__=="__main__":
	print(main())