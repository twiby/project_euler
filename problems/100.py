from math import sqrt

def main():
	N = 10**12

	b = 1
	last_b = 0

	sqrt_delta = 3
	last_sqrt_delta = 1
	while (4*b+1+sqrt_delta) < 2*N:
		b, last_b = 6*b - last_b, b
		sqrt_delta, last_sqrt_delta = 6*sqrt_delta - last_sqrt_delta, sqrt_delta
		
	return (2*b+1+sqrt_delta) // 2

if __name__=="__main__":
	print(main())
