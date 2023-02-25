def fib(N):
	prev = 1
	current = 1

	while current < N:
		yield current
		prev, current = current, prev + current

def main():
	N = 4000000
	sum = 0
	for i in fib(N):
		if i % 2 == 0:
			sum += i
	return sum

if __name__ == "__main__":
	print(main())