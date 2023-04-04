from itertools import combinations

def val_found(val, dice):
	if val in dice:
		return True
	elif val == 6 and 9 in dice:
		return True
	elif val == 9 and 6 in dice:
		return True
	else:
		return False
def pair_found(pair, dice_1, dice_2):
	if val_found(pair[0], dice_1) and val_found(pair[1], dice_2):
		return True
	elif val_found(pair[1], dice_1) and val_found(pair[0], dice_2):
		return True
	else:
		return False

def main():
	values = [i for i in range(10)]
	pairs = [[0,1], [0,4], [0,9], [1,6], [2,5], [3,6], [4,9], [6,4], [8,1]]

	count = 0
	for dice_1 in combinations(values, 6):
		for dice_2 in combinations(values, 6):
			all_found = True
			for pair in pairs:
				if not pair_found(pair, dice_1, dice_2):
					all_found = False
					break
			count += all_found

	return count//2

if __name__=="__main__":
	print(main())
