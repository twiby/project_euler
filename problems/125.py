def is_palindromic(n):
	chars = [c for c in str(n)]
	return chars[:len(chars)//2] == chars[-1:-len(chars)//2+len(chars)%2-1:-1]


def main():
	N = 1000
	N = 100000000

	max_nb_squares = 1
	val = 1
	while val < N:
		max_nb_squares += 1
		val += max_nb_squares*max_nb_squares
	max_nb_squares -= 1

	s = set()
	for nb_squares in range(2, max_nb_squares+1):
		val = sum([(1+i)*(1+i) for i in range(nb_squares)])
		diff = nb_squares
		while val < N:
			if is_palindromic(val):
				s.add(val)
			diff += 2
			val += diff*nb_squares

	return sum(s)

if __name__=="__main__":
	print(main())