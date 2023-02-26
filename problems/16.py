import numpy as np

def main():
	N = 1000
	return np.sum([int(c) for c in str(2**N)])

if __name__ == "__main__":
	print(main())