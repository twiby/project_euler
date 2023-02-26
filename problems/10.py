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

	return np.where(marked)


def main():
	N = 2000000
	return np.sum(sieve_prime(N))

if __name__ == "__main__":
	print(main())