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

def digit_gen_sqrt(D):
	cont_frac_gen = continued_frac_sqrt(D)

	first = next(cont_frac_gen)
	prevprev_x, prevprev_y = first, 1

	second = next(cont_frac_gen)
	x,y = first*second+1, second
	prev_x, prev_y = x, y

	curr = x/y
	for a_n in cont_frac_gen:
		x, y = a_n*prev_x + prevprev_x, a_n*prev_y + prevprev_y
		if abs(x/y - curr) < 0.00001:
			digit = x//y
			prev_x -= digit * prev_y
			x -= digit * y
			prev_x *= 10
			x *= 10
			yield digit
		curr = x/y
		prevprev_x, prevprev_y = prev_x, prev_y
		prev_x, prev_y = x, y

def main():
	squares = [4, 9, 16, 25, 36, 49, 64, 81]

	total = 0
	for K in range(2, 100):
		if K in squares:
			continue
		n = 0
		for d in digit_gen_sqrt(K):
			if n == 100:
				break
			total += d
			n += 1
	return total

if __name__=="__main__":
	print(main())