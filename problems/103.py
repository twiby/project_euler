from itertools import combinations

def special_sum_set(s):
	sums = [[sum(c) for c in combinations(s,n)] for n in range(1, len(s))]
	extrema = [(min(su), max(su)) for su in sums]

	for i in range(1, len(extrema)):
		if extrema[i][0] <= extrema[i-1][1]:
			return False

	total_set = set()
	for su in sums:
		if len(set(su)) < len(su):
			return False
		total_set.update(su)

	return len(total_set) == sum([len(su) for su in sums])

def next_guess(prev):
	med = prev[len(prev)//2]
	return [med] + [med+a for a in prev]

def main():
	guess = next_guess([6, 9, 11, 12, 13])

	current_sum = sum(guess)
	min_sum = current_sum
	best = guess
	n0 = guess[0]
	for n1 in range(12, (min_sum-n0-4-3-2-1)//5+1):
		for n2 in range(n1+1, min(n0+n1, (min_sum-n0-n1-3-2-1)//4+1)):
			for n3 in range(n2+1, min(n0+n1, (min_sum-n0-n1-n2-2-1)//3+1)):
				for n4 in range(n3+1, min(n0+n1, (min_sum-n0-n1-n2-n3-1)//2+1)):
					for n5 in range(n4+1, min(n0+n1, (min_sum-n0-n1-n2-n3-n4)+1)):
						lst = [n0,n1,n2,n3,n4,n5]
						if special_sum_set(lst) and sum(lst) < min_sum:
							min_sum = sum(lst)
							best = lst

	guess = next_guess(best)
	current_sum = sum(guess)
	min_sum = current_sum
	best = guess
	n0 = guess[0]
	for n1 in range(n0+1, (min_sum-n0-5-4-3-2-1)//6+1):
		for n2 in range(n1+1, min(n0+n1, (min_sum-n0-n1-4-3-2-1)//5+1)):
			for n3 in range(n2+1, min(n0+n1, (min_sum-n0-n1-n2-3-2-1)//4+1)):
				for n4 in range(n3+1, min(n0+n1, (min_sum-n0-n1-n2-n3-2-1)//3+1)):
					if not special_sum_set([n0,n1,n2,n3,n4]):
						continue
					for n5 in range(n4+1, min(n0+n1, (min_sum-n0-n1-n2-n3-n4-1)//2+1)):
						for n6 in range(n5+1, min(n0+n1, (min_sum-n0-n1-n2-n3-n4-n5))):
							lst = [n0,n1,n2,n3,n4,n5,n6]
							assert(sum(lst) < current_sum)
							if special_sum_set(lst) and sum(lst) < min_sum:
								min_sum = sum(lst)
								best = lst


	return "".join([str(i) for i in best])

if __name__=="__main__":
	print(main())