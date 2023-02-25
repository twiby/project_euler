import numpy as np

def pythagorean_triple(a,b,c):
	return c*c == a*a + b*b


def main():
	N = 1000
	for a in range(1, N):
		for b in range(a+1, N):
			c = N - a - b
			if c < b:
				continue
			elif pythagorean_triple(a,b,c):
				return a*b*c
	raise ValueError("Triplet not found")

if __name__ == "__main__":
	print(main())