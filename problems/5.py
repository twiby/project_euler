import numpy as np

class PrimeException(Exception):
	pass

def partial_factorize(n):
	for i in range(2, int(np.sqrt(n)) + 1):
		res = n / i
		if res == np.floor(res):
			return i, n/i
	raise PrimeException

def factorize(n, top=True):
	try:
		a, b = partial_factorize(n)
		return *factorize(a, False), *factorize(b, False)
	except PrimeException:
		return (int(n),)

def factor_count(n):
	ret = {}
	for f in factorize(n):
		if f in ret.keys():
			ret[f] += 1
		else:
			ret[f] = 1
	return ret

def develop_factors(factors):
	val = 1
	for k,v in factors.items():
		val *= k**v
	return val

def ppcm(f1,f2):
	ret = f1
	for k,v in f2.items():
		if k in ret.keys():
			ret[k] = np.max([ret[k], v])
		else:
			ret[k] = v
	return ret

def main():
	N = 20
	factors = {}
	
	for i in range(1, N):
		factors = ppcm(factors, factor_count(i))

	return develop_factors(factors)

if __name__ == "__main__":
	print(main())