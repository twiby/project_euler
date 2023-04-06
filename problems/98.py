import numpy as np

def nb_repeating_digit(n):
	word = [c for c in str(n)]
	return len(word) - len(set(word)) 

def main():
	with open("./data/p098_words.txt","r") as f:
		words = [[c for c in w[1:-1]] for l in f for w in l.split(",")]

	anagram_pairs = []
	for x in range(len(words)):
		for y in range(x):
			w1 = words[x].copy()
			w2 = words[y].copy()
			if len(w1) != len(w2):
				continue
			w1.sort()
			w2.sort()
			if w1 != w2:
				continue

			assert(len(set(w1)) >= len(w1)-1)
			anagram_pairs.append((words[x], words[y]))

	max_length = 0
	for w in anagram_pairs:
		if len(w[0]) > max_length:
			max_length = len(w[0])
	max_square = 10**max_length-1
	squares = [0, 1, 4, 9, 16]
	while squares[-1] < max_square:
		squares.append(len(squares)*len(squares))
	squares.pop()

	zerorep_digit_squares = []
	onerep_digit_squares = []
	for s in squares:
		val = nb_repeating_digit(s)
		if val == 0:
			zerorep_digit_squares.append(s)
		elif val == 1:
			onerep_digit_squares.append(s)
	zerorep_digit_squares = np.array(zerorep_digit_squares)
	onerep_digit_squares = np.array(onerep_digit_squares)

	while max_length > 0:
		square_anagrams = []
		for pair in anagram_pairs:
			length = len(pair[0])
			if length != max_length:
				continue

			if len(set(pair[0])) != length:
				possible_squares = onerep_digit_squares[np.logical_and(onerep_digit_squares >= 10**(length-1), onerep_digit_squares < 10**length-1)]

				for s in possible_squares:
					association = {c:n for c,n in zip(pair[0], str(s))}
					other = int("".join([association[c] for c in pair[1]]))
					if other in possible_squares:
						square_anagrams.append((s, other))
			else:
				possible_squares = zerorep_digit_squares[np.logical_and(zerorep_digit_squares >= 10**(length-1), zerorep_digit_squares < 10**length-1)]

				for s in possible_squares:
					association = {c:n for c,n in zip(pair[0], str(s))}
					other = int("".join([association[c] for c in pair[1]]))
					if other in possible_squares:
						square_anagrams.append((s, other))

		if len(square_anagrams):
			break
		max_length -= 1

	max = 0
	for s in square_anagrams:
		for ss in s:
			if ss > max:
				max = ss

	return max

if __name__=="__main__":
	print(main())
