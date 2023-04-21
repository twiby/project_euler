def nb_ways(N,M):
	nb_ways = [1]*M
	nb_ways.append(2)

	for i in range(M+1, N+1):
		n = nb_ways[i-1]
		n += nb_ways[i-M]
		nb_ways.append(n)

	return nb_ways[N] - 1


def main():
	return nb_ways(50, 2) + nb_ways(50, 3) + nb_ways(50, 4)

if __name__=="__main__":
	print(main())