def sum_multiples_of_k(k_list, N):
	sum  = {k:0 for k in k_list}
	count = [0 for _ in k_list]
	for i in range(1, N):
		for k in range(len(k_list)):
			count[k] += 1
			if count[k] == k_list[k]:
				sum[k_list[k]] += i
				count[k] = 0
	return sum

def main():
	N = 1000
	sums = sum_multiples_of_k([3, 5, 15], N)
	return sums[3] + sums[5] - sums[15]

if __name__ == "__main__":
	print(main())