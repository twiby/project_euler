def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)

def nth_lexicographic_permutation(n, elements):
	size = len(elements)
	if size == 1:
		return [elements[0]]

	partial_size = fact(size-1)
	first_digit = ((n-1) // partial_size) % size

	return [elements[first_digit]] + nth_lexicographic_permutation(n, elements[:first_digit] + elements[first_digit+1:])

def main():
	return "".join([str(n) for n in nth_lexicographic_permutation(1000000, [0,1,2,3,4,5,6,7,8,9])])

if __name__ == "__main__":
	print(main())