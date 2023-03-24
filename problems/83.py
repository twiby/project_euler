import sys
import numpy as np

test = np.array([
	[131, 673, 234, 103, 18],
	[201, 96, 342, 965, 150],
	[630, 803, 746, 422, 111],
	[537, 699, 497, 121, 956],
	[805, 732, 524, 37, 331],
])

def main():
	# weights = test.copy()
	with open("./data/p083_matrix.txt", "r") as f:
		weights = np.array([[int(s) for s in l.split(",")]for l in f])

	n = len(weights)
	inf = np.sum(weights) + 1
	visited = np.zeros_like(weights, dtype=bool)
	tentative_distances = np.zeros_like(weights, dtype=np.int64) + inf
	tentative_distances[0,0] = weights[0,0]

	for _ in range(n**n):
		current = np.unravel_index(np.argmin(tentative_distances + visited*inf), tentative_distances.shape)
		if current == (n-1, n-1):
			return tentative_distances[current]

		unvisited_neighbors = []
		if current[0] > 0 and not visited[current[0]-1, current[1]]:
			unvisited_neighbors.append((current[0]-1, current[1]))
		if current[1] > 0 and not visited[current[0], current[1]-1]:
			unvisited_neighbors.append((current[0], current[1]-1))
		if current[0] < n-1 and not visited[current[0]+1, current[1]]:
			unvisited_neighbors.append((current[0]+1, current[1]))
		if current[1] < n-1 and not visited[current[0], current[1]+1]:
			unvisited_neighbors.append((current[0], current[1]+1))

		for neighbor in unvisited_neighbors:
			tentative_distances[neighbor] = min(tentative_distances[neighbor], tentative_distances[current] + weights[neighbor])
		visited[current] = True

	print("Something unexpected happened")
	sys.exit(1)

if __name__=="__main__":
	print(main())