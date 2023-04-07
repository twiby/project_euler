from math import sqrt

PHI = (1+sqrt(5))/2
pandigital = set(["1","2","3","4","5","6","7","8","9"])

def fib_approx(n):
	ret = 1/sqrt(5)
	for i in range(n):
		ret *= PHI
		if ret > 10**9:
			ret /= 10**9
	return n, ret

def fib_approx_from_previous(n, prev):
	ret = prev[1]
	for i in range(prev[0], n):
		ret *= PHI
		while ret > 1:
			ret /= 10
	return n, ret

def last_digits_pandigital():
	a,b,n = 1,1,2
	while True:
		digits = [c for c in str(a)]
		if set(digits[-9:]) == pandigital:
			yield n
		a,b,n = a+b,a,n+1
		a %= 10**9
		b %= 10**9

def main():
	gen = last_digits_pandigital()

	prev = fib_approx(next(gen))
	for n in gen:
		new = fib_approx_from_previous(n, prev)
		digits = str(new[1])[2:11]
		if set(digits) == pandigital:
			return n
		prev = new

if __name__=="__main__":
	print(main())