some_numbers_string = {
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	7: "seven",
	8: "eight",
	9: "nine",
	10: "ten",
	11: "eleven",
	12: "twelve",
	13: "thirteen",
	14: "fourteen",
	15: "fifteen",
	16: "sixteen",
	17: "seventeen",
	18: "eighteen",
	19: "nineteen",
	20: "twenty",
	30: "thirty",
	40: "forty",
	50: "fifty",
	60: "sixty",
	70: "seventy",
	80: "eighty",
	90: "ninety",
	100: "hundred",
	1000: "onethousand"
}

def number_in_letters(n):
	if n == 1000:
		return "onethousand"

	if n <= 20:
		return some_numbers_string[n]
	elif n < 100:
		last_digit = n % 10
		if last_digit == 0:
			return some_numbers_string[n]
		else:
			return some_numbers_string[n - last_digit] + some_numbers_string[last_digit]
	else:
		last_2_digits = n % 100
		hundreds = (n - last_2_digits) // 100
		if last_2_digits == 0:
			return some_numbers_string[hundreds] + some_numbers_string[100]
		else:
			return some_numbers_string[hundreds] + some_numbers_string[100] + "and" + number_in_letters(last_2_digits)

def main():
	sum = 0
	for i in range(1, 1001):
		sum += len(number_in_letters(i))
	return sum

if __name__ == "__main__":
	print(main())