import numpy as np

square_names = {
	"GO": 0,
	"A1": 1,
	"CC1": 2,
	"A2": 3,
	"T1": 4,
	"R1": 5,
	"B1": 6,
	"CH1": 7,
	"B2": 8,
	"B3": 9,
	"JAIL": 10,
	"C1": 11,
	"U1": 12,
	"C2": 13,
	"C3": 14,
	"R2": 15,
	"D1": 16,
	"CC2": 17,
	"D2": 18,
	"D3": 19,
	"FP": 20,
	"E1": 21,
	"CH2": 22,
	"E2": 23,
	"E3": 24,
	"R3": 25,
	"F1": 26,
	"F2": 27,
	"U2": 28,
	"F3": 29,
	"G2J": 30,
	"G1": 31,
	"G2": 32,
	"CC3": 33,
	"G3": 34,
	"R4": 35,
	"CH3": 36,
	"H1": 37,
	"T2": 38,
	"H2": 39
}

def six_dice_probas():
	return np.array([0, 0, 1/36, 2/36, 3/36, 4/36, 5/36, 6/36,
			5/36, 4/36, 3/36, 2/36, 1/36])
def six_dice_three_doubles():
	return 1/(6*6*6)

def four_dice_probas():
	return np.array([0, 0, 1/16, 2/16, 3/16, 4/16, 3/16, 2/16, 1/16])
def four_dice_three_doubles():
	return 1/(4*4*4)

def move_by_roll(n):
	ret = np.zeros(40)
	roll = four_dice_probas()
	for idx in range(len(roll)):
		ret[(n + idx) % 40] = roll[idx]

	### Go to jail
	ret[square_names["JAIL"]] += ret[square_names["G2J"]]
	ret[square_names["G2J"]] = 0

	### Chance
	next_r = {
		"CH1": "R2",
		"CH2": "R3",
		"CH3": "R1"
	}
	next_u = {
		"CH1": "U1",
		"CH2": "U2",
		"CH3": "U1"
	}
	for ch in ["CH1", "CH2", "CH3"]:
		if not ret[square_names[ch]]:
			continue
		value = ret[square_names[ch]]
		ret[square_names[ch]] -= 10*value/16
		ret[square_names["GO"]] += value/16
		ret[square_names["JAIL"]] += value/16
		ret[square_names["C1"]] += value/16
		ret[square_names["E3"]] += value/16
		ret[square_names["H2"]] += value/16
		ret[square_names["R1"]] += value/16
		ret[square_names[next_r[ch]]] += 2*value/16
		ret[square_names[next_u[ch]]] += value/16
		ret[square_names[ch]-3] += value/16

	### Community chest
	for cc in ["CC1", "CC2", "CC3"]:
		if not ret[square_names[cc]]:
			continue
		value = ret[square_names[cc]]
		ret[square_names[cc]] -= 2*value/16
		ret[square_names["JAIL"]] += value/16
		ret[square_names["GO"]] += value/16

	return ret / np.sum(ret)

def main():
	probas = np.array([0.0 for _ in range(40)])
	probas[0] = 1

	for _ in range(500):
		new_probas = np.sum([probas[i] * move_by_roll(i) for i in range(40)], axis = 0)
		probas = new_probas

	### three doubles gets you to jail (this approach is probably wrong, 
	### but we only need an approxmation)
	go2jail_bydice_proba = four_dice_three_doubles()
	probas *= 1 - go2jail_bydice_proba
	probas[square_names["JAIL"]] += go2jail_bydice_proba

	most_probable_squares = np.argsort(1-probas)
	return most_probable_squares[0]*10000 + most_probable_squares[1]*100 + most_probable_squares[2]

if __name__=="__main__":
	print(main())