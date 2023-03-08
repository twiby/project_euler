def nb_ways(n, values):
	if len(values) == 1:
		return 1
	return sum([nb_ways(n-u*values[0], values[1:]) for u in range(n//values[0]+1)])

def main():
	return nb_ways(200, [200,100,50,20,10,5,2,1])

if __name__=="__main__":
	print(main())