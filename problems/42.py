A = bytes("A", "ascii")[0]
triangular_numbers = [1]

def word_value(string):
	return sum([val - A + 1 for val in bytes(string, "ascii")])

def compute_triangular_numbers_up_to(n):
	while triangular_numbers[-1] < n:
		triangular_numbers.append(triangular_numbers[-1]+len(triangular_numbers)+1)

def is_triangular_word(string):
	val = word_value(string)
	compute_triangular_numbers_up_to(val)
	return val in triangular_numbers

def main():
	count = 0
	with open("./data/p042_words.txt","r") as f:
		for word in (w[1:-1] for w in next(f).split(",")):
			if is_triangular_word(word):
				count += 1

	return count

if __name__=="__main__":
	print(main())