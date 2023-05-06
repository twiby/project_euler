import numpy as np

def sieve_prime(N):
	marked = np.ones(N, dtype=bool)
	marked[0] = False
	marked[1] = False
	target = int(np.sqrt(N))+1

	for current in range(2, target):
		if not marked[current]:
			continue
		marked[current*current::current] = False

	return marked, np.where(marked)[0]

def T(n):
	return n*(n+1)//2
def A(n):
	return 6 * T(n-1) + 2
def L(n):
	return A(n+1) - 1

def main():
	N = 834768
	sieve, primes = sieve_prime(N)

	max_PD = [1, 2]
	for n in range(2, N//12):
		if sieve[6*n-1] and sieve[6*n+1] and sieve[12*n+5]:
			max_PD.append(A(n))
		if sieve[6*n-1] and sieve[6*(n+1)-1] and sieve[12*(n-1)+5]:
			max_PD.append(L(n))
		if len(max_PD) >= 2000:
			break

	return max_PD[2000-1]

if __name__=="__main__":
	print(main())
