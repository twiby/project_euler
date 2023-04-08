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
	s = 0
	with open("./data/p105_sets.txt","r") as f:
		for l in f:
			if l[-1] == "\n":
				l = l[:-1]
			lst = [int(el) for el in l.split(",")]
			if special_sum_set(lst):
				s += sum(lst)

	return s

if __name__=="__main__":
	print(main())