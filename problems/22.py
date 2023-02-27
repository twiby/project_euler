
values = {
	"A": 1,
	"B": 2,
	"C": 3,
	"D": 4,
	"E": 5,
	"F": 6,
	"G": 7,
	"H": 8,
	"I": 9,
	"J": 10,
	"K": 11,
	"L": 12,
	"M": 13,
	"N": 14,
	"O": 15,
	"P": 16,
	"Q": 17,
	"R": 18,
	"S": 19,
	"T": 20,
	"U": 21,
	"V": 22,
	"W": 23,
	"X": 24,
	"Y": 25,
	"Z": 26,
}

def name_score(name):
	return sum(values[c] for c in name)

def main():
	with open("./data/p022_names.txt","r") as f:
		names = [name[1:-1] for name in next(f).split(',')]
	names.sort()

	sum = 0
	for n in range(len(names)):
		sum += (n+1) * name_score(names[n])

	return sum 

if __name__ == "__main__":
	print(main())
