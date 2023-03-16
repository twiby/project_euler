import numpy as np

def continued_frac_sqrt(n):
	sqrt_n = np.sqrt(n)
	first = int(sqrt_n)
	if first*first == n:
		return
	yield first

	a = n - first*first
	temp = int((first + sqrt_n)/a)
	yield temp
	b = temp*a - first

	while True:
		a = (n-b*b)//a
		temp = int((b+sqrt_n)/a)
		yield temp
		b = temp*a - b

def minimal_solution_via_cont_frac(D):
	cont_frac_gen = continued_frac_sqrt(D)

	first = next(cont_frac_gen)
	if first*first == D + 1:
		return first, 1
	prevprev_x, prevprev_y = first, 1

	second = next(cont_frac_gen)
	x,y = first*second+1, second
	if x*x - D*y*y == 1:
		return x,y
	prev_x, prev_y = x, y

	for a_n in cont_frac_gen:
		x, y = a_n*prev_x + prevprev_x, a_n*prev_y + prevprev_y
		if x*x - D*y*y == 1:
			return x, y
		prevprev_x, prevprev_y = prev_x, prev_y
		prev_x, prev_y = x, y

def main():
	N = 1000

	max = 0
	max_value = 0
	for D in range(N+1):
		test = int(np.sqrt(D))
		if test*test == D:
			continue
		x, y = minimal_solution_via_cont_frac(D)
		if x > max:
			max = x
			max_value = D

	return max_value

if __name__ == "__main__":
	print(main())
