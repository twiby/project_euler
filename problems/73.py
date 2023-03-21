def main():
	N = 12000

	a,b,c,d = 2,7,1,3
	a,b = a + c*((N-b)//d), b + d*((N-b)//d)

	count = 0
	q = ((N+b)//d)*d-b
	while q != 2:
		count += 1
		d, q = q, ((N+d)//q)*q-d

	return count

if __name__ == "__main__":
	print(main())
