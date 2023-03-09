def d(N):
	for n in range(N):
		for c in str(n):
			yield int(c)

def main():
	N = 1000000
	n = 0
	prod = 1
	for i in d(N):
		if n == 1 or n == 10 or n == 100 or n == 1000 or n == 10000 or n == 100000:
			prod *= i
		if n == 1000000:
			prod *= i
			break
		n += 1
		

	return prod

if __name__=="__main__":
	print(main())