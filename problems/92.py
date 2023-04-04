import numpy as np

def next(n):
	ret = 0
	while n:
		ret += (n%10)*(n%10)
		n //= 10
	return ret

def main():
	N = 10000000

	nb_digits_max = int(np.log10(N))
	end_up_89 = np.zeros(nb_digits_max*81+1, dtype=bool)
	for n in range(2, nb_digits_max * 81 + 1):
		i = n
		while True:
			i = next(i)
			if i == 1:
				end_up_89[n] = False
				break
			elif i == 89:
				end_up_89[n] = True
				break

	nexts = np.array([next(i) for i in range(N//10)])
	count = np.sum(end_up_89[nexts])

	for n in range(1, 10):
		full_nexts = n*n + nexts
		count += np.sum(end_up_89[full_nexts])

	return count

if __name__=="__main__":
	print(main())
