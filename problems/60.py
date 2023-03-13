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
	assert(False)
	for i in primes:
		if i*i > n:
			return True
		elif not n % i:
			return False
	assert(False)
	m = i % 6

	if m == 1:
		while i * i <= n:
			if n % i:
				i += 4
			else:
				return False
			if n % i:
				i += 2
			else:
				return False
	else:
		while i * i <= n:
			if n % i:
				i += 2
			else:
				return False
			if n % i:
				i += 4
			else:
				return False


	return True

def is_prime_pair(p1,p2, sieve, primes):
	try:
		return \
			is_prime(int(p1+p2), sieve, primes) and \
			is_prime(int(p2+p1), sieve, primes)
	except IndexError:
		return False

def prime_pairs(primes_str, primes, sieve):
	nb_dig = len(str(len(sieve)))
	max_nb_dig = nb_dig//2 if nb_dig%2 else nb_dig//2-1
	length = len(primes[np.where(primes < 10**(max_nb_dig))])
	for i1 in range(length):
		p1 = primes_str[i1]
		for i2 in range(i1):
			p2 = primes_str[i2]
			if is_prime_pair(p1,p2, sieve, primes):
				yield p2, p1




def main():
	N = 100000000
	sieve, primes = sieve_prime(N)
	primes_str = [str(p) for p in primes]

	prime_tuples_list = [p for p in prime_pairs(primes_str, primes, sieve)]
	filler_candidates = set(np.array(prime_tuples_list).flatten())

	for t in prime_tuples_list:
		for i in range(len(t)-1):
			assert(int(t[i+1])>int(t[i])) 

	prime_tuples_list_3 = []
	for t in prime_tuples_list:
		for p in filler_candidates:
			if int(p) >= int(t[0]):
				continue
			good = True
			for tt in t:
				if not is_prime_pair(p, tt, sieve, primes):
					good = False
					break
			if good:
				prime_tuples_list_3.append((p,) + t)	
	filler_candidates = set(np.array(prime_tuples_list_3).flatten())
	# print(prime_tuples_list_3, len(filler_candidates))

	for t in prime_tuples_list_3:
		for i in range(len(t)-1):
			assert(int(t[i+1])>int(t[i])) 


	prime_tuples_list_4 = []
	for t in prime_tuples_list_3:
		for p in filler_candidates:
			if int(p) >= int(t[0]):
				continue
			good = True
			for tt in t:
				if not is_prime_pair(p, tt, sieve, primes):
					good = False
					break
			if good:
				prime_tuples_list_4.append((p,)+t)
	filler_candidates = set(np.array(prime_tuples_list_4).flatten())
	# print(prime_tuples_list_4, len(filler_candidates))

	for t in prime_tuples_list_4:
		for i in range(len(t)-1):
			assert(int(t[i+1])>int(t[i])) 

	prime_tuples_list_5 = []
	for t in prime_tuples_list_4:
		for p in filler_candidates:
			if int(p) >= int(t[0]):
				continue
			good = True
			for tt in t:
				if not is_prime_pair(p, tt, sieve, primes):
					good = False
					break
			if good:
				prime_tuples_list_5.append((p,)+t)
	filler_candidates = set(np.array(prime_tuples_list_5).flatten())
	# print(prime_tuples_list_5, len(filler_candidates))

	for t in prime_tuples_list_5:
		for i in range(len(t)-1):
			assert(int(t[i+1])>int(t[i])) 

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