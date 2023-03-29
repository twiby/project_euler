import numpy as np

def tri(a):
	return a*(a+1)//2

def main():
	N = 2000000

	dim = int(np.sqrt(2*N))

	T_b = np.array([tri(b) for b in range(dim)])
	N_ab = np.array([tri(a) * T_b for a in range(dim)])
	best_val = np.unravel_index(np.argmin(np.abs(N_ab-N)), N_ab.shape)
	return best_val[0] * best_val[1]

if __name__=="__main__":
	print(main())