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

def main():
	N = 100000
	sieve, primes = sieve_prime(N)


	nb = 0
	s = 0
	for p in primes:
		if not (p % 40) in [1,9,11,17,21,31,33]:
			s += p
			continue

		mod = 1
		log_10_mod_p = 10 % p
		already_seen = set([1])
		for i in range(p):
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
			temp += log_10_mod_p
			log_10_mod_p = (log_10_mod_p*prev) % p
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

			if mod == 0:
				break
			elif mod in already_seen:
				nb += 1
				s += p
				break
			already_seen.add(mod)

	return s


if __name__=="__main__":
	print(main())
