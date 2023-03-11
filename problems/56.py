def main():
	max = 0
	for a in range(100):
		for b in range(100):
			s = sum(int(c) for c in str(a**b))
			if s > max:
				max = s
	return max

if __name__ == "__main__":
	print(main())