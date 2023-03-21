fact = {
	"0": 1,
	"1": 1,
	"2": 2,
	"3": 6,
	"4": 24,
	"5": 120,
	"6": 720,
	"7": 7*720,
	"8": 7*8*720,
	"9": 7*8*9*720,
}

def next_str(string):
	ret = str(sum([fact[c] for c in string]))
	ret = [c for c in ret]
	ret.sort()
	return "".join(ret)

def chain_of_non_repeating_terms_with_table(n, table):
	if n in table.keys():
		return table[n], []
	lst = [n]
	while True:
		n = next_str(n)
		if n in lst:
			return len(lst), lst
		elif n in table.keys():
			return len(lst) + table[n], lst
		lst.append(n)

def sorted_str(n):
	digits = [c for c in str(n)]
	digits.sort()
	return "".join(digits)

def sorted_digits(nb_digits):
	ret = [0 for _ in range(nb_digits)]
	yield ret

	while ret != [9 for _ in range(nb_digits)]:
		if ret[-1] == 9:
			cursor = nb_digits - 2
			while ret[cursor] == 9:
				cursor -= 1
			ret[cursor] += 1
			for c in range(cursor, nb_digits):
				ret[c] = ret[cursor]
			yield ret
		else:
			ret[-1] += 1
			yield ret

def sorted_strings(nb_digits):
	for digits in sorted_digits(nb_digits):
		yield "".join([str(d) for d in digits])

def num_permutation(string):
	ret = fact[str(len(string))]
	d = 0
	while d<len(string) and string[d] == "0":
		ret -= fact[str(len(string)-d-1)]
		d += 1
	couplings = {}
	for d in range(1, len(string)):
		if string[d-1] == string[d]:
			if string[d] in couplings.keys():
				couplings[string[d]] += 1
			else:
				couplings[string[d]] = 2
	for val in couplings.values():
		ret //= fact[str(val)]
	return ret

def main():
	N = 1000000
	K = 60

	count = 0
	table = {}
	for nb_digits in range(1, 7):
		for i in sorted_strings(nb_digits):

			table[i], lst = chain_of_non_repeating_terms_with_table(i, table)

			minus = 1
			for el in lst[1:]:
				table[el] = table[i] - minus
				minus += 1

	for (k,v) in table.items():
		if v == K:
			count += num_permutation(k)

	return count

if __name__ == "__main__":
	print(main())
