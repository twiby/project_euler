def main():
	N = 99

	count = 0

	checkouts_1 = []
	for i in range(1, 21):
		#### simple
		if i <= N:
			checkouts_1.append([["S"+str(i)], i])

		#### double
		if 2*i <= N:
			count += 1
			checkouts_1.append([["D"+str(i)], 2*i])

		#### triple
		if 3*i <= N:
			checkouts_1.append([["T"+str(i)], 3*i])
	i = 25
	#### simple
	if i <= N:
		checkouts_1.append([["S"+str(i)], i])

	#### double
	if 2*i <= N:
		count += 1
		checkouts_1.append([["D"+str(i)], 2*i])

	checkouts_2 = []
	for c in checkouts_1:
		prev_darts, prev_score = c
		for i in range(1, 21):
			#### simple
			if prev_score + i <= N:
				checkouts_2.append([prev_darts + ["S"+str(i)], prev_score + i])

			#### double
			if prev_score + 2*i <= N:
				count += 1
				checkouts_2.append([prev_darts + ["D"+str(i)], prev_score + 2*i])

			#### triple
			if prev_score + 3*i <= N:
				checkouts_2.append([prev_darts + ["T"+str(i)], prev_score + 3*i])
		i = 25
		#### simple
		if prev_score + i <= N:
			checkouts_2.append([prev_darts + ["S"+str(i)], prev_score + i])

		#### double
		if prev_score + 2*i <= N:
			count += 1
			checkouts_2.append([prev_darts + ["D"+str(i)], prev_score + 2*i])

	for c in checkouts_2:
		prev_darts, prev_score = c
		for i in range(1, 21):
			#### double
			if prev_score + 2*i <= N:
				count += prev_darts[1] >= prev_darts[0]
		#### double
		if prev_score + 50 <= N:
			count += prev_darts[1] >= prev_darts[0]

	return count

if __name__=="__main__":
	print(main())