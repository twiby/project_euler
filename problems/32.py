import numpy as np

def pandigital(a,b):
	string = str(a) + str(b) + str(a*b)
	if len(string) != 9:
		return False
	s = set([c for c in string])
	if s==set(["1","2","3","4","5","6","7","8","9"]):
		return True
	return False

def nb_digits(n):
	return int(np.log10(n))+1

def main():
	s = set()
	for a in range(2, 10000):
		na = nb_digits(a)
		b = 2
		while na + nb_digits(b) + nb_digits(a*b) < 10:
			if pandigital(a,b):
				s.add(a*b)
			b += 1 
	return sum(s)

if __name__=="__main__":
	print(main())