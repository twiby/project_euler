def i_to_the_nth_mod(i, n, modulus, i_mod):
	if n == 1:
		return i_mod
	if n%2==0:
		return (i_to_the_nth_mod(i, n//2, modulus,i_mod)**2)%modulus
	else:
		return (i_mod*i_to_the_nth_mod(i,n-1, modulus,i_mod))%modulus

def main():
	nb_digits = 10
	modulus = 10**nb_digits

	N = 1000

	val = sum([i_to_the_nth_mod(i,i,modulus,i%modulus) for i in range(1,N)]) % modulus

	### case begin with 0
	string = str(val)
	while len(string) < 10:
		string = "0" + string

	return string

if __name__ == "__main__":
	print(main())
