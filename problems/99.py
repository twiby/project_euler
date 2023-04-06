import numpy as np

def main():
	base_exp = []
	with open("./data/p099_base_exp.txt","r") as f:
		for l in f:
			if l[-1] == "\n":
				l = l[:-1]
			base_exp.append([int(el) for el in l.split(",")])

	logs = [be[1] * np.log(be[0]) for be in base_exp]
	return np.argmax(logs)+1

if __name__=="__main__":
	print(main())
