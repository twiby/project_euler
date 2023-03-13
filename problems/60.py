import sys
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

def is_prime(n, sieve, primes):
	if n < len(sieve):
		return sieve[n]

	for i in primes:
		if i*i > n:
			return True
		elif not n % i:
			return False
	return False

order = [1, 10, 100, 1000, 10000]
def is_prime_pair(p1,p2,d1,d2, sieve, primes):
	return (is_prime(p1+p2*order[d1], sieve, primes)) and \
		(is_prime(p2+p1*order[d2], sieve, primes))

def sub_primes_pairs(primes_1, primes_str_1, primes, sieve, nb_digits, ret):
	length = len(primes_1[np.where(primes_1 < 10**nb_digits)])
	for i1 in range(1,length):
		p1 = primes_1[i1]
		d1 = len(primes_str_1[i1])
		for p2,d2 in zip(primes_1[1:i1], primes_str_1[1:i1]):

			if is_prime_pair(p1,p2,d1,len(d2),sieve, primes):
				ret.append((p2,p1))

def prime_pairs(nb_digits, primes, sieve):
	primes_1 = primes[np.where(primes%3 == 1)]
	primes_2 = primes[np.where(primes%3 == 2)]
	primes_str_1 = np.array([str(p) for p in primes_1])
	primes_str_2 = np.array([str(p) for p in primes_2])

	ret = []
	sub_primes_pairs(primes_1.copy(), primes_str_1.copy(), primes.copy(), sieve.copy(), nb_digits, ret)
	sub_primes_pairs(primes_2.copy(), primes_str_2.copy(), primes.copy(), sieve.copy(), nb_digits, ret)

	return ret



def main():
	N = 10000
	sieve, primes = sieve_prime(N)

	prime_tuples_list = prime_pairs(4, primes, sieve)
	pairs = set(prime_tuples_list)
	filler_candidates = set(np.array(prime_tuples_list).flatten())

	for t in prime_tuples_list:
		for i in range(len(t)-1):
			assert(int(t[i+1])>int(t[i])) 

	prime_tuples_list_3 = []
	for t in prime_tuples_list:
		for p in filler_candidates:
			if p >= t[0]:
				continue
			good = True
			for tt in t:
				if not (p,tt) in pairs:
					good = False
					break
			if good:
				prime_tuples_list_3.append((p,) + t)	
	filler_candidates = set(np.array(prime_tuples_list_3).flatten())

	prime_tuples_list_4 = []
	for t in prime_tuples_list_3:
		for p in filler_candidates:
			if p >= t[0]:
				continue
			good = True
			for tt in t:
				if not (p,tt) in pairs:
					good = False
					break
			if good:
				prime_tuples_list_4.append((p,)+t)
	filler_candidates = set(np.array(prime_tuples_list_4).flatten())

	prime_tuples_list_5 = []
	for t in prime_tuples_list_4:
		for p in filler_candidates:
			if p >= t[0]:
				continue
			good = True
			for tt in t:
				if not (p,tt) in pairs:
					good = False
					break
			if good:
				prime_tuples_list_5.append((p,)+t)

	if len(prime_tuples_list_5) > 0:
		max_sum = 0
		for t in prime_tuples_list_5:
			s = sum([int(c) for c in t])
			if s > max_sum:
				max_sum = s
		return max_sum


	print("Buffer too small")
	sys.exit(1)

if __name__ == "__main__":
	print(main())
