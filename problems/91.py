import numpy as np

def main():
	N = 50

	s = 0
	s2 = 0
	for x1 in range(N+1):
		for y1 in range(1, N+1):
			d1 = x1*x1 + y1*y1
			for x2 in range(max(1, x1), N+1):
				for y2 in range(y1+1):
					if x1==x2 and y1==y2:
						continue
					d2 = x2*x2 + y2*y2
					d3 = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
					if d3==d1+d2 or d1==d2+d3 or d2==d1+d3:
						s += 1

	return s

if __name__=="__main__":
	print(main())
