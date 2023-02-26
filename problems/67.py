test = [
[3],
[7, 4],
[2, 4, 6],
[8, 5, 9, 3],
]

def main():
	tree = []
	with open("./p067_triangle.txt", "r") as f:
		for l in f:
			tree.append([int(c) for c in l[:-1].split(" ")])

	cursor = len(tree) - 1
	current_best = tree[cursor]
	cursor -= 1
	while cursor >= 0:
		line = tree[cursor]
		current_best = [line[i]+max(current_best[i], current_best[i+1]) for i in range(len(line))]
		cursor -= 1

	return current_best[0]
	
if __name__ == "__main__":
	print(main())

