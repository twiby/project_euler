
def main():
	N = 10**10
	ret = 28433

	for _ in range(7830457//4):
		ret *= 16
		ret %= N

	ret *= 2
	ret += 1
	ret %= N
	return ret

if __name__=="__main__":
	print(main())
