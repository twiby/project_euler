def nb_sorted_numbers_with_k_digits_and_first_digit_at_least_d(k, d):
	if k == 1:
		return 10-d
	else:
		ret = 0
		for i in range(d, 10):
			ret += nb_sorted_numbers_with_k_digits_and_first_digit_at_least_d(k-1, i)
		return ret

def nb_sorted_numbers_with_k_digits_and_first_digit_at_least_d_2(k, d, prev):
	if k == 1:
		return 10-d
	else:
		ret = 0
		for i in range(d, 10):
			ret += prev[i]
		return ret

def _nb_reversed_numbers_with_k_digits_end_first_digit_max_d(k, d):
	if k == 1:
		return d + 1
	else:
		ret = 0
		for i in range(d+1):
			ret += _nb_reversed_numbers_with_k_digits_end_first_digit_max_d(k-1, i)
		return ret
def nb_reversed_numbers_with_k_digits_end_first_digit_max_d(k,d):
	return _nb_reversed_numbers_with_k_digits_end_first_digit_max_d(k,d) - 1
def nb_reversed_numbers_with_k_digits_end_first_digit_max_d_2(k, d, prev):
	if k == 1:
		return d + 1
	else:
		ret = 0
		for i in range(0, d+1):
			ret += prev[i] + 1
		return ret-1

def main():
	N_digits_target = 100

	prev = [nb_sorted_numbers_with_k_digits_and_first_digit_at_least_d(4, d) for d in range(10)]
	nb_sorted = [100, nb_sorted_numbers_with_k_digits_and_first_digit_at_least_d(3, 1), prev[1]]

	for i in range(5, N_digits_target):
		prev = [nb_sorted_numbers_with_k_digits_and_first_digit_at_least_d_2(i, d, prev) for d in range(10)]
		nb_sorted.append(prev[1])

	nb_sorted.append(nb_sorted_numbers_with_k_digits_and_first_digit_at_least_d_2(N_digits_target, 1, prev))


	prev = [nb_reversed_numbers_with_k_digits_end_first_digit_max_d(4, d) for d in range(10)]
	nb_reversed = [nb_reversed_numbers_with_k_digits_end_first_digit_max_d(3, 9)-9, prev[-1]-9]

	for i in range(5, N_digits_target):
		prev = [nb_reversed_numbers_with_k_digits_end_first_digit_max_d_2(i, d, prev) for d in range(10)]
		nb_reversed.append(prev[-1]-9)
	nb_reversed.append(nb_reversed_numbers_with_k_digits_end_first_digit_max_d_2(N_digits_target, 9, prev)-9)

	return sum(nb_sorted) + sum(nb_reversed) - 1

if __name__=="__main__":
	print(main())