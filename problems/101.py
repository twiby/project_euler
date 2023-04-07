import numpy as np

def evaluate(poly, n):
	val = 1
	ret = 0
	for coef in poly:
		ret += val*coef
		val *= n
	return ret

def evaluate_all(poly):
	return [evaluate(poly, n) for n in range(1, len(poly))]

def main():
	actual = np.array([0,0,0,1])
	actual2 = np.array([1,-1,1,-1,1,-1,1,-1,1,-1,1])

	values = evaluate_all(actual2)
	sum = values[0]
	for degree in range(2, len(values)+1):
		inputs = np.ones((degree, degree))
		for i in range(degree):
			for d in range(degree):
				inputs[i,d] = (i+1)**d
		bad_poly = np.linalg.inv(inputs) @ values[:degree]
		sum += int(evaluate(bad_poly, degree+1).round())
	return sum

if __name__=="__main__":
	print(main())