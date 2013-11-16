from factorization.primegen import primegen

def factors(n):
	"""generator function yielding the prime factors of n
	Heavily derived from http://en.wikipedia.org/wiki/Trial_division
	>>> list(factors(14))
	[2, 7]
	>>> list(factors(13195))
	[5, 7, 13, 29]
	>>> list(factors(8))
	[2, 2, 2]
	
	"""

	for p in primegen(int(n**0.5) + 1):
		# sqrt(n) < p => n = q * (p^k), where k is 0 or 1, and q is product of each element of factors
		if p*p > n:
			break
		# append factor for each time it appears
		while not n%p:
			yield p
			n = n / p
	if n > 1:
		yield n

if __name__ == '__main__':
	import doctest
	doctest.testmod()