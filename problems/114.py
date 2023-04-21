def main():
	nb_ways = [1, 1, 1, 2]

	for i in range(4, 51):
		n = nb_ways[i-1]

		for k in range(4, i+1):
			n += nb_ways[i-k]
		nb_ways.append(n+1)

	return nb_ways[50]

if __name__=="__main__":
	print(main())