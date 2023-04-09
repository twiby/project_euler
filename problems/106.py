from itertools import combinations

def main():
	s = set([1,2,3,4,5,6,7,8,9,10,11,12])
	ret = []
	for comb_size in range(2, len(s)//2+1):
		combos = [c for c in combinations(s, comb_size)]
		for c in combos:
			for cc in combinations(s-set(c), comb_size):
				if c[0] > cc[0]:
					continue
				all_good = False
				for i in range(len(c)):
					if c[i] > cc[i]:
						all_good = True
						break
				if all_good:
					ret.append((c, cc))

	return len(ret)

if __name__=="__main__":
	print(main())