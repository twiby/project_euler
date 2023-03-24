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
	with open("./data/p081_matrix.txt", "r") as f:
		shortest_path = np.array([[int(s) for s in l.split(",")]for l in f])

	for n in range(1, len(shortest_path)):
		shortest_path[0, n] += shortest_path[0, n-1]
		shortest_path[n, 0] += shortest_path[n-1, 0]

		for i in range(1, n):
			shortest_path[i, n] += min(shortest_path[i-1, n], shortest_path[i, n-1])
			shortest_path[n, i] += min(shortest_path[n-1, i], shortest_path[n, i-1])

		shortest_path[n,n] += min(shortest_path[n-1, n], shortest_path[n, n-1])

	return shortest_path[-1, -1]

if __name__=="__main__":
	print(main())