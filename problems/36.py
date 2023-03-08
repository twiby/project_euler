
def string_palindromic(s):
	if len(s) == 1:
		return True

	half = list(s[:len(s)//2])
	half_rev = list(s[-len(s)//2+len(s)%2:])
	half_rev.reverse()
	return half == half_rev

def deci_palindromic(n):
	return string_palindromic(str(n))
def bin_palindromic(n):
	return string_palindromic("{0:b}".format(n))

def num(digits):
	return sum([digits[i]*(10**(len(digits)-i-1)) for i in range(len(digits))])
	
def palindrom_from_pattern(n):
	if n < 10:
		yield n

	digits_rev = [int(c) for c in str(n)]
	digits_rev.reverse()
	n_rev = num(digits_rev)

	n *= 10**len(digits_rev)
	yield n + n_rev
	
	n *= 10
	for i in range(10):
		yield n + n_rev + i*(10**len(digits_rev))

def main():
	N = 1000000
	N_pattern = 1000

	sum = 0
	for n in range(N_pattern):
		for p in palindrom_from_pattern(n):
			if p > N:
				break
			if bin_palindromic(p):
				sum += p

	return sum

if __name__=="__main__":
	print(main())
