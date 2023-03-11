from enum import Enum

class HandType(Enum):
	HighCard = 1
	OnePair = 2
	TwoPairs = 3
	ThreeKind = 4
	Straight = 5
	Flush = 6
	FullHouse = 7
	FourKind = 8
	StraightFlush = 9
	RoyalFlush = 10

strength = {
	"2": 0,
	"3": 1,
	"4": 2,
	"5": 3,
	"6": 4,
	"7": 5,
	"8": 6,
	"9": 7,
	"T": 8,
	"J": 9,
	"Q": 10,
	"K": 11,
	"A": 12,
}

def default_values():
	return {i:0 for i in range(13)}

def same_suit(c1,c2):
	return c1[1] == c2[1]

def same_value(c1,c2):
	return c1[0] == c2[0]

def counts(hand):
	val = default_values()
	for c in hand:
		val[c[0]] += 1
	return {k: v for k, v in val.items() if v}

def get_hands(play):
	play = play.split(" ")
	h1 = [(strength[c[0]],c[1]) for c in play[:5]]
	h2 = [(strength[c[0]],c[1]) for c in play[5:]]
	h1.sort(key = lambda c:c[0])
	h2.sort(key = lambda c:c[0])
	return h1,h2

def get_hand_type(h, val):
	flush = True
	for i in range(1, 5):
		if h[i][1] != h[0][1]:
			flush = False
			break

	straight = True
	for i in range(1,5):
		if h[i][0] != h[i-1][0]+1:
			straight = False
			break

	if straight and flush:
		if h[0][0] == strength["T"]:
			return HandType.RoyalFlush
		else:
			return HandType.StraightFlush
	elif straight:
		return HandType.Straight
	elif flush:
		return HandType.Flush

	typology = set(val.values())

	if typology == set([4,1]):
		return HandType.FourKind
	elif typology == set([3,2]):
		return HandType.FullHouse
	elif typology == set([3,1,1]):
		return HandType.ThreeKind
	elif typology == set([1,1,1,1,1]):
		return HandType.HighCard
	
	exact_values = list(val.values())
	exact_values.sort()
	if exact_values == [1,2,2]:
		return HandType.TwoPairs
	elif exact_values == [1,1,1,2]:
		return HandType.OnePair

	raise ValueError

def tie_breaker(counts_1, counts_2):
	sorted_1 = [(-v,-k) for k,v in counts_1.items()]
	sorted_2 = [(-v,-k) for k,v in counts_2.items()]
	sorted_1.sort()
	sorted_2.sort()

	for i in range(len(sorted_1)):
		if sorted_1[i][1] < sorted_2[i][1]:
			return 1
		elif sorted_1[i][1] > sorted_2[i][1]:
			return 0
	raise ValueError

def winner(play):
	h1, h2 = get_hands(play)
	counts_1, counts_2 = counts(h1), counts(h2)

	hand_type_1 = get_hand_type(h1, counts_1)
	hand_type_2 = get_hand_type(h2, counts_2)
	
	if hand_type_1.value > hand_type_2.value:
		return 1
	elif hand_type_1.value < hand_type_2.value:
		return 0
	else:
		return tie_breaker(counts_1, counts_2)

def main():
	count = 0
	with open("./data/p054_poker.txt","r") as f:
		for play in f:
			count += winner(play[:-1])

	return count

if __name__ == "__main__":
	print(main())