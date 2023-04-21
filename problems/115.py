def main():
	M = 50

	nb_ways = [1] * (M+1)
	nb_ways[M] = 2

	i = M+1
	while True:
		n = nb_ways[i-1]

		for k in range(M+1, i+1):
			n += nb_ways[i-k]
		nb_ways.append(n+1)

		if nb_ways[-1] >= 1000000:
			return i
		i += 1

if __name__=="__main__":
	print(main())