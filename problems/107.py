import numpy as np

def min_tree(network):
	return _min_tree(network, used = [0])

def _min_tree(network, current_sum = 0, used = [0]):
	if len(used) == len(network):
		return current_sum

	best = (-1, np.sum(network))
	for i in range(len(network)):
		if i in used or (network[i, used] == 0).all():
			continue

		best_branch = min(network[i, used][network[i,used]>0])
		if best_branch < best[1]:
			best = (i, best_branch)

	return _min_tree(network, current_sum = current_sum + best[1], used = used + [best[0]])


def main():
	network = np.array([
		[0, 16, 12, 21, 0, 0, 0],
		[16, 0, 0, 17, 20, 0, 0],
		[12, 0, 0, 28, 0, 31, 0],
		[21, 17, 28, 0, 18, 19, 23],
		[0, 20, 0, 18, 0, 0, 11],
		[0, 0, 31, 19, 0, 0, 27],
		[0, 0, 0, 23, 11, 27, 0],
	])

	network = np.zeros((40,40), dtype=np.int64)
	with open("./data/p107_network.txt", "r") as f:
		y = 0
		for l in f:
			if l[-1] == "\n":
				l = l [:-1]
			x = -1
			for el in l.split(","):
				x += 1
				if el == "-":
					continue
				network[x,y] = int(el)
			y += 1

	min_tree_weight = min_tree(network)

	tot = np.sum(network)//2
	return tot - min_tree_weight

if __name__=="__main__":
	print(main())