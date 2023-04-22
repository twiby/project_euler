def main():
	N = 50
	nb_ways = [1, 1, 2, 4, 8]

	for i in range(5, N+1):
		n = nb_ways[i-1]
		n += nb_ways[i-2]
		n += nb_ways[i-3]
		n += nb_ways[i-4]
		nb_ways.append(n)

	print(nb_ways[N])

	return 0

if __name__=="__main__":
	print(main())