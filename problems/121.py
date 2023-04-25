
def next(prev_turn):
	next_turn = [0 for _ in prev_turn]
	next_turn.append(0)
	n = len(prev_turn) - 1

	for k in range(len(prev_turn)):
		next_turn[k+1] += prev_turn[k] / (n+2)
		next_turn[k] += prev_turn[k] * (n+1) / (n+2)

	return next_turn

def more_blue(turn):
	ret = 0
	for n in range(len(turn)):
		if n <= len(turn)-n-1:
			continue
		ret += turn[n]
	return ret

def main():
	turns_old = [1]

	for i in range(15):
		turns_old = next(turns_old)

	return int(1/more_blue(turns_old))


if __name__=="__main__":
	print(main())