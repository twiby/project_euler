import numpy as np
from fractions import Fraction

def is_continued_frac_sqrt_odd_period(n):
	sqrt_n = np.sqrt(n)
	first = int(sqrt_n)
	if first*first == n:
		return False

	a = n - first*first
	temp = int((first + sqrt_n)/a)
	b = -(first - temp*a)

	odd_cycle = True
	while (a,b) != (1,first):
		a = (n-b*b)//a
		temp = int((b+sqrt_n)/a)
		b = -(b - temp*a)

		odd_cycle = not odd_cycle
	return odd_cycle

def main():
	N = 10000

	count = 0
	for n in range(N+1):
		if is_continued_frac_sqrt_odd_period(n):
			count += 1

	
	return count

if __name__ == "__main__":
	print(main())
