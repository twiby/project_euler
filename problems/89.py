
def compute_unity(string):
	if "X" in string:
		return 9
	elif "V" in string:
		return 4
	else:
		return len(string)

def compute_tens(string):
	if "L" in string:
		return 40
	elif "C" in string:
		return 90
	else:
		return 10*len(string)

def compute_hundreds(string):
	if "D" in string:
		return 400
	elif "M" in string:
		return 900
	else:
		return 100*len(string)

def compute_num(numeral):
	val = 0

	if "I" in numeral:
		idx = 0
		while numeral[idx] != "I":
			idx += 1
		val += compute_unity(numeral[idx:])
		numeral = numeral[:idx]

	if len(numeral) == 0:
		return val

	if numeral[-1] == "V":
		val += 5
		numeral = numeral[:-1]

	if len(numeral) == 0:
		return val

	if "X" in numeral:
		idx = 0
		while numeral[idx] != "X":
			idx += 1
		val += compute_tens(numeral[idx:])
		numeral = numeral[:idx]

	if len(numeral) == 0:
		return val

	if numeral[-1] == "L":
		val += 50
		numeral = numeral[:-1]

	if len(numeral) == 0:
		return val

	if "C" in numeral:
		idx = 0
		while numeral[idx] != "C":
			idx += 1
		val += compute_hundreds(numeral[idx:])
		numeral = numeral[:idx]

	if len(numeral) == 0:
		return val

	if numeral[-1] == "D":
		val += 500
		numeral = numeral[:-1]

	if len(numeral) == 0:
		return val

	return 1000*len(numeral)+val

def roman(val):
	ret = ""
	thousands = val // 1000
	ret += "M"*thousands
	val %= 1000

	hundreds = val // 100
	if hundreds == 9:
		ret += "CM"
	elif hundreds == 4:
		ret += "CD"
	else:
		if hundreds >= 5:
			ret += "D"
			hundreds -= 5
		ret += "C" * hundreds
	val %= 100

	tens = val // 10
	if tens == 9:
		ret += "XC"
	elif tens == 4:
		ret += "XL"
	else:
		if tens >= 5:
			ret += "L"
			tens -= 5
		ret += "X" * tens
	val %= 10

	if val == 9:
		ret += "IX"
	elif val == 4:
		ret += "IV"
	else:
		if val >= 5:
			ret += "V"
			val -= 5
		ret += "I"*val
	return ret

def main():
	s = 0
	with open("./data/p089_roman.txt","r") as f:
		for l in f:
			if l[-1] == "\n":
				l = l[:-1]
			s += len(l) - len(roman(compute_num(l)))
	return s

if __name__=="__main__":
	print(main())