def solve(a):
	max = 0
	for n in range(1, a+1):
		val = (2*a*n) % (a*a)
		if val > max:
			max = val
	return max

def main():
	N = 1000

	s = 0
	for a in range(3, N + 1):
		s += solve(a)
	return s

if __name__=="__main__":
	print(main())