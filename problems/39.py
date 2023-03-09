import numpy as np

def other_side(p, b):
	return p*(p-2*b)/2/(p-b)

def nb_solutions(p):
	count = 0
	for b in range(1, int(p/(2 + np.sqrt(2)))):
		a = other_side(p,b)
		if a != int(a):
			continue
		c = np.sqrt(a**2 + b**2)
		if c != int(c):
			continue
		count += 1
	return count

def main():
	N = 1000

	max = 3
	max_value = 120

	for n in range(25, N):
		nb = nb_solutions(n)
		if nb > max:
			max = nb
			max_value = n
	return max_value

if __name__=="__main__":
	print(main())