import numpy as np

def enumerate_pythagorean_triple(N):
	order = int(np.sqrt(N/2))+1
	a,b,c,d = 1,order,1,order-1

	if (a+b)%2:	
		yield (b*b-a*a, 2*a*b, a*a+b*b)
	if (c+d)%2:
		yield (d*d-c*c, 2*c*d, c*c+d*d)

	p, q = c*((order+b)//d) - a, d*((order+b)//d) - b
	while (p,q) != (1,1):
		if (p+q)%2:
			yield (q*q-p*p, 2*p*q, c*c+d*d)
		p, q = c*((order+b)//d) - a, d*((order+b)//d) - b
		a,b,c,d = c,d,p,q

def main():

	N = 1500000

	table = np.zeros(N, dtype=np.int64)
	for triple in enumerate_pythagorean_triple(N):
		p = sum(triple)
		if p < N:
			table[p::p] += 1
	return len(np.where(table == 1)[0])

if __name__ == "__main__":
	print(main())
