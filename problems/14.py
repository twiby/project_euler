import numpy as np

def collatz(n):
	if n % 2 == 0:
		return n // 2
	else:
		return 3*n + 1

def chain_length(n):
	count = 1
	while n > 1:
		count += 1
		n = collatz(n)
	return count

def chain_length_with_history(n, chains):
	count = 1
	while n > 1:
		count += 1
		if n < len(chains) and chains[n] > 0:
			return count + chains[n] - 2
		n = collatz(n)
	return count

def main():
	N = 1000000

	chains_old = np.zeros(N, dtype=int)

	chains = np.zeros(N, dtype=int)
	for n in range(1, N):
		chains[n] = chain_length_with_history(n, chains)
	return np.argmax(chains)

if __name__ == "__main__":
	print(main())