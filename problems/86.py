import sys
import numpy as np

def enumerate_pythagorean_triple(N):
	order = int(np.sqrt(N))+1
	a,b,c,d = 1,order,1,order-1

	if (a+b)%2:	
		yield (b*b-a*a, 2*a*b, a*a+b*b)
	if (c+d)%2:
		yield (d*d-c*c, 2*c*d, c*c+d*d)

	p, q = c*((order+b)//d) - a, d*((order+b)//d) - b
	while (p,q) != (1,1):
		if (p+q)%2:
			yield (q*q-p*p, 2*p*q, p*p+q*q)
		p, q = c*((order+b)//d) - a, d*((order+b)//d) - b
		a,b,c,d = c,d,p,q

def main():
	N = 2000
	max_L = N*np.sqrt(5)
	counts= np.zeros(N, dtype = np.int64)

	for t in enumerate_pythagorean_triple(max_L):
		if t[2] > max_L:
			continue

		for n in range(1, N//t[1]+1):
			counts[n*t[1]:] += max((n*t[0] - 2*max(1, n*(t[0]-t[1])) + 2)//2, 0)

		for n in range(1, N//t[0]+1):
			counts[n*t[0]:] += max((n*t[1] - 2*max(1, n*(t[1]-t[0])) + 2)//2, 0)

	try:
		return np.min(np.where(counts > 1000000))
	except:
		print("Buffer too small")
		sys.exit(1)

if __name__=="__main__":
	print(main())