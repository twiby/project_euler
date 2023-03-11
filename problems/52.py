import sys

def main():
	N = 200000

	for n in range(1, N):
		s1 = set([int(c) for c in str(n)])

		all_good = True
		for m in range(2,7):
			if s1 != set([int(c) for c in str(m*n)]):
				all_good = False
				break
		if all_good:
			return n

	print("Buffer too small")
	sys.exit(1)

if __name__ == "__main__":
	print(main())