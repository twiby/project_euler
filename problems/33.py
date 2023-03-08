

def main():
	l = []
	for a in range(10, 100):
		for b in range(a+1, 100):
			a_d = [a%10, a//10]
			b_d = [b%10, b//10]
			if 0 in a_d or 0 in b_d:
				continue

			if b_d[0] == a_d[0]:
				new_a = a_d[1]
				new_b = b_d[1]
			elif b_d[0] == a_d[1]:
				new_a = a_d[0]
				new_b = b_d[1]
			elif b_d[1] == a_d[0]:
				new_a = a_d[1]
				new_b = b_d[0]
			elif b_d[1] == a_d[1]:
				new_a = a_d[0]
				new_b = b_d[0]
			else:
				continue

			if new_a/new_b == a/b:
				l.append([new_a,new_b])

	p = [1,1]
	for ll in l:
		p[0] *= ll[0]
		p[1] *= ll[1]
	return int(p[1] / p[0])

if __name__=="__main__":
	print(main())