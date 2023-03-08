import numpy as np

def fact(n):
	if n == 1 or n == 0:
		return 1
	else:
		return n * fact(n-1)

def one_digit_more_of_factorials(n_digit, fact_list):
	zero = fact_list.copy()

	input = fact_list.copy()
	size = len(fact_list)
	size //= 10
	while size > 1:
		input[:size] += 1
		size //= 10

	return np.concatenate([zero]+[input+zero[i] for i in range(1, 10)])


def main():
	digit_fact = np.array([fact(n) for n in range(10)])
	max_nb_digits = 1
	while digit_fact[9]*max_nb_digits > 10**max_nb_digits:
		max_nb_digits += 1
	max_value = digit_fact[9] * max_nb_digits


	all_facts = digit_fact.copy()
	for d in range(2, max_nb_digits + 1):
		all_facts = one_digit_more_of_factorials(d, all_facts)

	indices = np.array([n for n in range(max_value)])
	return sum(np.where(indices == all_facts[:max_value])[0][2:])

if __name__=="__main__":
	print(main())