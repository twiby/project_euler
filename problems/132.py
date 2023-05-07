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

def ten_to_the_5_to_the_k_mod_p(k, p):
	mod = 10 % p
	for i in range(k):
		mod_sqr = mod * mod
		mod_sqr %= p

		mod *= mod_sqr * mod_sqr
		mod %= p
	return mod

def main():
	N = 1000000
	sieve, primes = sieve_prime(N)


	nb = 0
	s = 0
	for p in primes:
		mod = 1
		log_10_mod_p = 10 % p
		temp = 1
		for i in range(9):
			prev = log_10_mod_p
			temp = 1
			temp += log_10_mod_p
			log_10_mod_p = (log_10_mod_p*prev) % p
			temp += log_10_mod_p
			log_10_mod_p = (log_10_mod_p*prev) % p
			temp += log_10_mod_p
			log_10_mod_p = (log_10_mod_p*prev) % p
			temp += log_10_mod_p
			log_10_mod_p = (log_10_mod_p*prev) % p
			temp %= p
			mod *= temp
			mod %= p

		base = ten_to_the_5_to_the_k_mod_p(9, p)
		for i in range(9):
			mod *= base + 1
			mod %= p
			base *= base
			base %= p
		if mod == 0:
			nb += 1
			s += p
			if nb == 40:
				return s

if __name__=="__main__":
	print(main())
