month_duration = {
	0: 31,
	1: 28,
	2: 31,
	3: 30,
	4: 31,
	5: 30,
	6: 31,
	7: 31,
	8: 30,
	9: 31,
	10: 30,
	11: 31
}

def is_leap_year(year):
	if year % 100 == 0:
		return year % 400 == 0
	else:
		return year % 4 == 0

def one_week_later(date):
	wl = [date[0] + 7, date[1], date[2]]
	month = month_duration[date[1]]
	if date[1] == 2 and is_leap_year(date[2]):
		month += 1

	if wl[0] > month:
		wl = [wl[0] - month, date[1] + 1, date[2]]
	if wl[1] == 12:
		wl = [wl[0], 0, wl[2] + 1]
	return wl

def main():
	date = [6, 0, 1901]

	count = 1
	while date[2] < 2001:
		if date[0] == 1:
			count += 1
		date = one_week_later(date)


	return count
	
if __name__ == "__main__":
	print(main())

