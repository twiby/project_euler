
def main():
	N = 9999

	max = 0
	while N > 0:
		string = str(N)

		n = 2
		while len(string) < 9:
			string += str(n*N)
			n += 1 

		if len(string) > 9:
			N-=1
			continue

		if set([c for c in string]) == set(["1","2","3","4","5","6","7","8","9"]) and int(string) > max:
			max = int(string)

		N -= 1

	return max

if __name__=="__main__":
	print(main())