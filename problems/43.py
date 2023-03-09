def num(digits):
	return int("".join([str(i) for i in digits]))

def permut(v, n=0):
	if len(v)-1 == n:
		yield v
		return

	for i in range(n,len(v)):
		if n == 3 and v[i]%2 != 0:
			continue
		elif n == 4 and (v[2]+v[3]+v[i])%3!=0:
			continue
		elif n == 5 and not v[i] in [0,5]:
			continue
		elif n == 6 and num([v[4],v[5],v[i]])%7!=0:
			continue
		elif n == 7 and num([v[5],v[6],v[i]])%11!=0:
			continue
		elif n == 8 and num([v[6],v[7],v[i]])%13!=0:
			continue
		assert(n!=9)
		v[i],v[n]=v[n],v[i]
		yield from permut(v, n+1)
		v[i],v[n]=v[n],v[i]
	


def main():
	sum = 0
	for p in permut([0,1,2,3,4,5,6,7,8,9]):
		if num(p[-3:])%17==0:
			sum += num(p)
	return sum

if __name__=="__main__":
	print(main())