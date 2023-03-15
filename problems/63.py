import numpy as np

def main():
	count = 0
	curr_pow = 1
	sub_count = 1

	while sub_count > 0:
		sub_count = 0

		if curr_pow == 1:
			n = 1
		else:
			n = int(10**((curr_pow-1)/curr_pow))+1

		while int(curr_pow*np.log10(n))+1 == curr_pow:
			sub_count += 1
			n += 1
		if sub_count == 0:
			break
		count += sub_count
		curr_pow += 1

	return count

if __name__ == "__main__":
	print(main())