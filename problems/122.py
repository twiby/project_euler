import numpy as np

def main():
	N = 200

	all_results = [[2]]

	m = np.array([0 for _ in range(N+1)])
	m[2] = 1
	for k in range(8):
		next = []
		for l in all_results:
			next.append(l + [1+l[-1]])
			for ll in l:
				next.append(l + [ll + l[-1]])

		to_remove = []
		first = None
		for idx in range(len(next)):
			l = next[idx]
			if l[-1] > N:
				to_remove.append(idx)
				continue
			if m[l[-1]] == 0:
				if first is None:
					first = idx
				# print(k, idx, l)
				m[l[-1]] = len(l)
			# else:
			# 	to_remove.append(idx)

		all_results = []
		for idx in range(len(next)):
			if not idx in to_remove:
				all_results.append(next[idx])

	all_results = [[2]]
	m2 = np.array([0 for _ in range(N+1)])
	m2[2] = 1
	for k in range(8):
		next = []
		for l in all_results:
			next.append(l + [1+l[-1]])
			for ll in l:
				next.append(l + [ll + l[-1]])

		to_remove = []
		first = None
		for idx in range(len(next)):
			l = next[idx]
			if l[-1] > N:
				to_remove.append(idx)
				continue
			if m2[l[-1]] == 0:
				if first is None:
					first = idx
				# print(k, idx, l)
				m2[l[-1]] = len(l)
			else:
				to_remove.append(idx)

		all_results = []
		for idx in range(len(next)):
			if not idx in to_remove:
				all_results.append(next[idx])

	error = len(np.where(m != m2)[0])

	all_results = [[2]]
	m2 = np.array([0 for _ in range(N+1)])
	m2[2] = 1
	for k in range(10):
		next = []
		for l in all_results:
			next.append(l + [1+l[-1]])
			for ll in l:
				next.append(l + [ll + l[-1]])

		to_remove = []
		first = None
		for idx in range(len(next)):
			l = next[idx]
			if l[-1] > N:
				to_remove.append(idx)
				continue
			if m2[l[-1]] == 0:
				if first is None:
					first = idx
				# print(k, idx, l)
				m2[l[-1]] = len(l)
			else:
				to_remove.append(idx)

		all_results = []
		for idx in range(len(next)):
			if not idx in to_remove:
				all_results.append(next[idx])

	return np.sum(m2) - error

if __name__=="__main__":
	print(main())