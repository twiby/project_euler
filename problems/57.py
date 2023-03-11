from fractions import Fraction

def expansions_sqrt_2():
	f = Fraction(3,2)
	while True:
		yield f
		f = 1 + 1/(1+f)

def digit_imbalance(f):
	return len(str(f.numerator)) > len(str(f.denominator))

def main():
	N = 1000
	
	n = 0
	count = 0
	for f in expansions_sqrt_2():
		if n > N:
			break
		count += digit_imbalance(f)
		n += 1

	return count

if __name__ == "__main__":
	print(main())