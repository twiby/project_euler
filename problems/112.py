def nb_sorted_numbers_with_k_digits_and_first_digit_at_least_d(k, d, max_digit = 9):
	if k == 1:
		return max_digit-d+1
	else:
		ret = 0
		for i in range(d, max_digit+1):
			ret += nb_sorted_numbers_with_k_digits_and_first_digit_at_least_d(k-1, i, max_digit)
		return ret

def _nb_reversed_numbers_with_k_digits_end_first_digit_max_d(k, d, min_digit = 0):
	if k == 1:
		return d - min_digit + 1
	else:
		ret = 0
		for i in range(min_digit, d+1):
			ret += _nb_reversed_numbers_with_k_digits_end_first_digit_max_d(k-1, i, min_digit)
		return ret
def nb_reversed_numbers_with_k_digits_end_first_digit_max_d(k,d):
	return _nb_reversed_numbers_with_k_digits_end_first_digit_max_d(k,d) - 1

def nb_bouncy_with_n_digits(n):
	if n < 3:
		return 0
	return 10**n - ((10**(n-1) - nb_bouncy_with_n_digits(n-1)) + nb_reversed_numbers_with_k_digits_end_first_digit_max_d(n, 9) + nb_sorted_numbers_with_k_digits_and_first_digit_at_least_d(n, 1) - 9)

def is_sorted(digits):
	for d in range(1, len(digits)):
		if digits[d] < digits[d-1]:
			return False
	return True
def is_unsorted(digits):
	for d in range(1, len(digits)):
		if digits[d] > digits[d-1]:
			return False
	return True
def is_bouncy(n):
	digits = [int(c) for c in str(n)]
	return not (is_sorted(digits) or is_unsorted(digits))

def main():
	start = 6
	stop = 7
	total = nb_bouncy_with_n_digits(start)

	for k in range(10**start, 10**stop):
		total += is_bouncy(k)
		if total >= 0.99*k:
			return k

	return 0

if __name__=="__main__":
	print(main())