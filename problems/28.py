import numpy as np

def up_right_diag(N):
	n = 3
	while n<=N:
		yield n**2
		n += 2 

def up_left_diag(N):
	n = 3
	for d in up_right_diag(N):
		yield d - n + 1
		n += 2
def bottom_left_diag(N):
	n = 3
	for d in up_left_diag(N):
		yield d - n + 1
		n += 2
def bottom_right_diag(N):
	n = 3
	for d in bottom_left_diag(N):
		yield d - n + 1
		n += 2

def main():
	N = 1001

	sum = 1
	sum += np.sum([n for n in up_right_diag(N)])
	sum += np.sum([n for n in up_left_diag(N)])
	sum += np.sum([n for n in bottom_left_diag(N)])
	sum += np.sum([n for n in bottom_right_diag(N)])
	return sum

if __name__=="__main__":
	print(main())