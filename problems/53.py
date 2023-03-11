import numpy as np

def new_binomials(old_binomials):
	ret = np.ones(len(old_binomials) + 1)
	n = len(old_binomials)
	for k in range(1,n//2+1):
		ret[k] = old_binomials[k-1] + old_binomials[k]
		if ret[k] > 1000000:
			ret[k] = float('nan')
	for k in range(n//2+1,n):
		ret[k] = ret[n-k]
	return ret

def main():
	n = 2
	binomials = np.array([1,2,1])

	count = 0
	while len(binomials) <= 100:
		binomials = new_binomials(binomials)
		count += np.sum(np.isnan(binomials))

	return count

if __name__ == "__main__":
	print(main())
