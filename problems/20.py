
def fact(n):
	if n <= 1:
		return 1
	else:
		return n * fact(n-1)

def main():
	return sum([int(c) for c in str(fact(100))])

if __name__ == "__main__":
	print(main())
