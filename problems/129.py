
def A(n):
	if n % 2 == 0 or n % 5 == 0:
		raise ValueError

	k = 1
	m = 1
	while m != 0:
		m = (10*m + 1) % n
		k += 1
	return k

def main():
	N = 1000000

	for n in range(N//10, N):
		for last_digit in [1,3,7,9]:
			val = 10*n + last_digit
			if A(val) > N:
				return val

	return 0

if __name__=="__main__":
	print(main())
