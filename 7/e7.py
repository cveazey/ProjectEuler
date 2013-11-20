#!/usr/bin/env python

from factorization.primegen import primegen

def prime_at_index(index,upper):
	""" does what it says kinda
	>>> prime_at_index(10000,200000)
	104743
	"""
	primes = list(primegen(upper))
	try:
		return primes[index]
	except IndexError:
		raise ValueError("upper bound not high enough")
	
def main():
	upper = 200000
	while True:
		try:
			p = prime_at_index(10000,upper)
			break
		except ValueError:
			upper += 100000
			print('too few primes, incrementing upper to {0}'.format(upper))
	print('10001st prime = {0}'.format(p))

if __name__ == '__main__':
	main()