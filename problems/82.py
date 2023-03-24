import numpy as np

test = np.array([
	[131, 673, 234, 103, 18],
	[201, 96, 342, 965, 150],
	[630, 803, 746, 422, 111],
	[537, 699, 497, 121, 956],
	[805, 732, 524, 37, 331],
])

def main():
	# shortest_path = test.copy()
	with open("./data/p082_matrix.txt", "r") as f:
		shortest_path = np.array([[int(s) for s in l.split(",")]for l in f])

	for n in range(1, len(shortest_path)):

		shortest = shortest_path[:, n-1] + shortest_path[:, n]

		path_down = shortest.copy()
		path_up = shortest.copy()
		for i in range(1, len(shortest_path)):
			path_down[:-i] += shortest_path[i:, n]
			shortest[i:] = np.min([path_down[:-i], shortest[i:]], axis = 0)

			path_up[i:] += shortest_path[:-i, n]
			shortest[:-i] = np.min([path_up[i:], shortest[:-i]], axis = 0)

		shortest_path[:, n] = shortest

	return min(shortest_path[:, -1])

if __name__=="__main__":
	print(main())