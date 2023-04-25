import numpy as np
from itertools import permutations

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

def is_prime(n, sieve, primes):
	if n < len(sieve):
		return sieve[n]
	max_factor = int(np.sqrt(n))
	for i in primes:
		if i > max_factor:
			break
		elif not n%i:
			return False
	return True

def nb_sets(cleaned_primes, sieve, primes, primes_without, start_idx = 0, exclude_digits = set()):
	s = 0
	current_digits = set([1,2,3,4,5,6,7,8,9]) - exclude_digits
	sel = np.array([True for _ in cleaned_primes])
	sel[:start_idx] = False
	for d in exclude_digits:
		sel = np.logical_and(sel, primes_without[d])

	for p_idx in range(start_idx, len(cleaned_primes)):
		if not sel[p_idx]:
			continue
		
		p = cleaned_primes[p_idx]
		digits = set([int(c) for c in str(p)])

		ok_digits = current_digits - digits
		if len(ok_digits) < len(digits):
			break

		if sum(ok_digits)%3:
			for new_p in permutations(ok_digits):
				new_p = int("".join([str(c) for c in new_p]))
				if new_p > p and is_prime(new_p, sieve, primes):
					s += 1

		new_excluded = exclude_digits.copy()
		new_excluded.update(digits)
		s += nb_sets(cleaned_primes, sieve, primes, primes_without, start_idx = p_idx + 1, exclude_digits = new_excluded)
	return s



def main():
	N = 1000000000
	sieve, primes = sieve_prime(10000000)

	cleaned_primes = []
	for p in primes:
		if p > int(np.sqrt(N)):
			break
		p_str = str(p)
		digits = set([int(c) for c in p_str])
		if len(digits) == len(p_str) and not 0 in digits:
			cleaned_primes.append(p)

	primes_without = {i: [False for _ in cleaned_primes] for i in range(1, 10)}
	for p_idx in range(len(cleaned_primes)):
		p = cleaned_primes[p_idx]
		digits = [int(c) for c in str(p)]
		for i in range(1, 10):
			if not i in digits:
				primes_without[i][p_idx] = True

	return nb_sets(cleaned_primes, sieve, primes, primes_without)

if __name__=="__main__":
	print(main())