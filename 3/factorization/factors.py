from factorization.primegen import primegen

def factors(n):
	"""Return a list of the prime factors of n
	Heavily derived from http://en.wikipedia.org/wiki/Trial_division
	>>> factors(14)
	[2, 7]
	>>> factors(13195)
	[5, 7, 13, 29]
	"""
	primes = primegen(int(n**0.5) + 1)
	factors = []
	for p in primes:
		# sqrt(n) < p => n = q * (p^k), where k is 0 or 1, and q is product of each element of factors
		if p*p > n:
			break
		# append factor for each time it appears
		while not n%p:
			factors.append(p)
			n = n / p
	if n > 1:
		factors.append(n)

	return factors

if __name__ == '__main__':
	import doctest
	doctest.testmod()