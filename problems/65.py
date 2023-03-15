import numpy as np
from fractions import Fraction

def continued_frac_e(N):
	if N == 0:
		return

	yield 2

	mod_3 = 2
	k = 1
	while mod_3 < N+1:
		if mod_3 % 3:
			yield 1
		else:
			yield 2*k
			k += 1
		mod_3 += 1

#### this turns out wrong for one third of the values
def convergents_e(trunc_cont_frac):
	f = Fraction(1, trunc_cont_frac[-1])
	for i in range(1,len(trunc_cont_frac)):
		val = trunc_cont_frac[-i-1]
		f = 1/f + val
	return f


def main():
	hundredth_convergent = convergents_e([c for c in continued_frac_e(100)])
	return sum([int(c) for c in str(hundredth_convergent.numerator)])

if __name__ == "__main__":
	print(main())