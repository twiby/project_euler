def main():
	N = 1000000000

	alpha, last_alpha = 1, 0
	perimeters = []
	while True:
		temp = alpha
		alpha = 4*alpha - last_alpha
		sqrt_delta = alpha - last_alpha
		last_sqrt_delta = sqrt_delta
		last_alpha = temp

		for b in [1, -1]:
			k = sqrt_delta + b*4
			if k%6 or k == 0:
				continue
			k //= 6
			perimeters.append(6*k-b-b)
			if perimeters[-1] > N:
				perimeters.pop()
				return sum(perimeters)

if __name__=="__main__":
	print(main())