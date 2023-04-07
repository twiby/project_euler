import numpy as np

def isInsideTriangle(A, B, C):
 
	# Calculate the barycentric coordinates
	# of point P with respect to triangle ABC
	denominator = ((B[1] - C[1]) * (A[0] - C[0]) +
	           (C[0] - B[0]) * (A[1] - C[1]))
	a = ((C[1] - B[1]) * C[0] +
	 (B[0] - C[0]) * C[1]) / denominator
	b = ((A[1] - C[1]) * C[0] +
	 (C[0] - A[0]) * C[1]) / denominator
	c = 1 - a - b

	# Check if all barycentric coordinates
	# are non-negative
	if a >= 0 and b >= 0 and c >= 0:
		return True
	else:
		return False

def main():
	count = 0
	with open("./data/p102_triangles.txt","r") as f:
		for l in f:
			if l[-1] == "\n":
				l = l[:-1]
			tri = np.array([int(c) for c in l.split(",")]).reshape((3,2))
			count += isInsideTriangle(tri[0,:], tri[1,:], tri[2,:])
	return count

if __name__=="__main__":
	print(main())