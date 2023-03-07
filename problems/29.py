
def main():
	N = 100

	s = set()
	for a in range(2, N+1):
		for b in range(2, N+1):
			s.add(a**b)

	return len(s)

if __name__=="__main__":
	print(main())