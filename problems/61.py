import numpy as np

def triangular(n):
	return n*(n+1)//2
def square(n):
	return n*n
def pentagonal(n):
	return n*(3*n-1)//2
def hexagonal(n):
	return n*(2*n-1)
def heptagonal(n):
	return n*(5*n-3)//2
def octogonal(n):
	return n*(3*n-2)
def num_gen(fun):
	n = 1
	while True:
		yield fun(n)
		n += 1

def get_numbers(gen):
	ret = [set() for _ in range(100)]
	while (n := next(gen)) < 10000:
		last_2 = n % 100
		first_2 = n // 100
		ret[first_2].add(last_2)
	return ret

def chains(numbers, chained_val = None, chain = None):
	if len(numbers) == 0:
		yield chain
		return

	if chained_val is None:
		for s in range(100):
			for n in numbers[0][s]:
				N = s*100 + n
				yield from chains(numbers[1:], chained_val = n, chain = [N])
	else:
		for nums_idx in range(len(numbers)):
			for n in numbers[nums_idx][chained_val]:
				N = chained_val*100 + n
				yield from chains(numbers[:nums_idx]+numbers[nums_idx+1:], chained_val = n, chain = chain + [N])


def main():
	number_generators = [num_gen(triangular), num_gen(square), num_gen(pentagonal), num_gen(hexagonal), num_gen(heptagonal), num_gen(octogonal)]

	numbers = [get_numbers(gen) for gen in number_generators]

	for chain in chains(numbers):
		if chain[0]//100 == chain[-1]%100 and (np.array(chain) > 999).all():
			return np.sum(chain)

if __name__ == "__main__":
	print(main())
