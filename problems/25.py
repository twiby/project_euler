import numpy as np

PHI1 = (1 - np.sqrt(5)) / 2
PHI2 = (1 + np.sqrt(5)) / 2


def log10(n):
	return np.log(n) / np.log(10.0)

def main():
	N = 1000

	return int(np.floor((N-1 + 0.5*log10(5)) / log10(PHI2))) + 1

if __name__ == "__main__":
	print(main())
