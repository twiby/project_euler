def palindrom(n):
	string = str(n)
	repeating_digits = len(string) // 2
	return bool(string[:repeating_digits] == string[-repeating_digits:][::-1])

def all_products(min, max):
	for n1 in range(min, max):
		for n2 in range(n1, max):
			yield n1 * n2

def two_digits_mult():
	yield from all_products(10, 100)
def three_digits_mult():
	yield from all_products(100, 1000)

def main():
	max = 0
	for i in three_digits_mult():
		if palindrom(i) and i > max:
			max = i
	return max

if __name__ == "__main__":
	print(main())