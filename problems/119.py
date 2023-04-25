def main():
	N = 1000
	all = set()

	for n in range(N):
		for pow in range(2,10):
			dig = [int(c) for c in str(n**pow)]
			if len(dig) > 1 and sum(dig) == n:
				all.add(n**pow)

	lst = list(all)
	lst.sort()

	return lst[29]

if __name__=="__main__":
	print(main())