def palindrom(n):
	string = str(n)
	repeating_digits = len(string) // 2
	return bool(string[:repeating_digits] == string[-repeating_digits:][::-1])

def reverse_digits(n):
	digits = [str(c)for c in str(n)]
	return int("".join(digits[::-1]))

def main():
	N = 10000

	count = 0
	for n in range(1, N):
		nn = n
		lychrel = True
		for i in range(51):
			n += reverse_digits(n)
			if palindrom(n):
				lychrel = False
				break
		count += lychrel

	return count

if __name__ == "__main__":
	print(main())