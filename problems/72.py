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

def main():
	N = 1000001
	sieve, primes = sieve_prime(N)

	# totients = np.array([i for i in range(N)])
	# totients[::2] //= 2
	# for i in primes[1:]:
	# 	totients[i::i] //= i
	# 	totients[i::i] *= i-1
	# return sum(totients)-1

	moebius = np.ones(N, dtype=np.int64)
	moebius[0] = 0
	for p in primes:
		moebius[p::p] *= -1
	for p in primes:
		square = p*p
		moebius[square::square] = 0

	moebius[N//3+1:N//2+1] *= ((N-1)//(N//3+1))**2
	moebius[N//4+1:N//3+1] *= ((N-1)//(N//4+1))**2
	moebius[N//5+1:N//4+1] *= ((N-1)//(N//5+1))**2
	moebius[N//6+1:N//5+1] *= ((N-1)//(N//6+1))**2
	for k in range(1,N//6+1):
		val = ((N-1)//k)*((N-1)//k)
		moebius[k] *= val
	return int((sum(moebius[1:])-1)//2)


if __name__ == "__main__":
	print(main())