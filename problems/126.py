import numpy as np

def T(n):
	return n*(n+1)//2

def cov1_2d(a,b):
	return 2*a + 2*b
def cov2_2d(a,b):
	return 2*a + 2*b + 4
def cov3_2d(a,b):
	return 2*a + 2*b + 8
def cov4_2d(a,b):
	return 2*a + 2*b + 12

def cov1(a,b,c):
	return c * cov1_2d(a,b) + 2*a*b
def cov2(a,b,c):
	return c * cov2_2d(a,b) + 2*a*b + 4*a + 4*b
def cov3(a,b,c):
	return c * cov3_2d(a,b) + 2*a*b + 8*a + 8*b + T(1)*8
def cov4(a,b,c):
	return c * cov4_2d(a,b) + 2*a*b + 12*a + 12*b + T(2)*8

def cov(n,a,b,c):
	return 2*a*b + 2*b*c + 2*a*c + n*4*(a+b+c) + T(n-1)*8

def coverture_size(a,b,c):
	return 2*(a*c+a*b+b*c)
### max a: 2*(a+2) = N
### max b: b = (N-2*a)//(2*a+2)
### max c: c = (N-2*a*b)//(2*a+2*b)


def main():
	N = 18523

	C = np.zeros(N, dtype=np.uint64)

	triangulars = np.array([T(i-1) for i in range(68)])*8
	linear_term = np.array([i for i in range(68)])*4

	for a in range(1, (N-4)//2+1):
		for b in range(a, (N-2*a)//(2*a+2)+1):
			for c in range(b, (N-2*a*b)//(2*a+2*b)+1):
				layers = 2*(a*c+a*b+b*c) + (a+b+c)*linear_term + triangulars
				C[layers[layers < N]] += 1

	return np.where(C == 1000)[0][0]

if __name__=="__main__":
	print(main())