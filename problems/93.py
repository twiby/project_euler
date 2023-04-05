from itertools import permutations

def mul(a,b):
	return a*b
def add(a,b):
	return a+b
def div(a,b):
	return a/b
def sub(a,b):
	return a-b

def all_results(a,b,c,d):
	ops = [mul, add, div, sub]
	s = set()
	for op1 in ops:
		for op2 in ops:
			for op3 in ops:
				for op4 in ops:
					val = op3(op2(op1(a,b),c),d)
					if int(val) == val and val > 0:
						s.add(int(val))
						
					val = op3(op1(a,b),op2(c,d))
					if int(val) == val and val > 0:
						s.add(int(val))
	return s


def main():
	max = 28
	max_value = [1,2,3,4]
	for a in range(1,7):
		for b in range(a+1, 8):
			for c in range(b+1, 9):
				for d in range(c+1, 10):
					s = set()
					for t in permutations([a,b,c,d]):
						s.update(all_results(*t))
					n = 1
					while n in s:
						n += 1
					n -= 1
					if n > max:
						max = n
						max_value = [a,b,c,d]

	return 1000*max_value[0] + 100*max_value[1] + 10*max_value[2] + max_value[3]

if __name__=="__main__":
	print(main())