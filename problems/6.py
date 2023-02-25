import numpy as np

def main():
	N = 100
	sum = 0
	sum_sq = 0
	for i in range(N+1):
		sum += i
		sum_sq += i*i
	return sum*sum - sum_sq

if __name__ == "__main__":
	print(main())