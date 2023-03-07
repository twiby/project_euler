import numpy as np

exponent = 5


def set_compatible(indices):
	val = np.sum(np.array(indices)**exponent)
	digits = [int(c) for c in str(val)]
	for i in digits:
		if not i in indices:
			return False
		indices.remove(i)
	if len(indices) == 0:
		return True
	for i in indices:
		if i != 0:
			return False
	return True


def main():
	sum = 0
	for i1 in range(10):
		for i2 in range(i1, 10):
			for i3 in range(i2, 10):
				for i4 in range(i3, 10):
					for i5 in range(i4, 10):
						for i6 in range(i5, 10):
							if set_compatible([i1,i2,i3,i4,i5,i6]):
								sum += np.sum(np.array([i1,i2,i3,i4,i5,i6])**exponent)


	return sum-1

if __name__=="__main__":
	print(main())