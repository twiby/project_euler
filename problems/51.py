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

def main():
	N = 1000000
	max_nb_digits = int(np.log10(N))

	sieve, primes = sieve_prime(N)

	series_size = 8

	new_digits = 2
	nb_digits_to_replace = 3
	nb_digits_tot = nb_digits_to_replace + new_digits

	while nb_digits_tot <= max_nb_digits:
		for places in itertools.combinations([i for i in range(nb_digits_tot-1)], new_digits-1):
			digits = ["*" for _ in range(nb_digits_tot)]
			digits[-1] = "d"
			for p in places:
				digits[p] = "d"
			
			for d0 in ["1","3","7","9"]:
				digits[-1] = d0
				for d in range(10**(new_digits-1)):
					digits_to_test = [c for c in str(d)]
					digits_to_test = ["0"]*(new_digits - 1 - len(digits_to_test)) + digits_to_test
					assert(len(places) == len(digits_to_test))
					for d,p in zip(digits_to_test, places):
						digits[p] = d
					if digits[0] == "0":
						continue
					false_count = 0
					found_value = None
					for v in ["0","1","2","3","4","5","6","7","8","9"]:
						if false_count > 10-series_size:
							break
						digits_full = [d if d!="*" else v for d in digits]
						# print(v, digits_full)
						if digits_full[0] == "0":
							false_count += 1
							continue
						val = int("".join(digits_full))
						if not sieve[val]:
							false_count += 1
							continue
						if found_value == None:
							found_value = val
					if false_count <= 10-series_size:
						return found_value
		new_digits += 1
		nb_digits_tot = nb_digits_to_replace + new_digits

	print("Buffer too small")
	sys.exit(1)

if __name__ == "__main__":
	print(main())