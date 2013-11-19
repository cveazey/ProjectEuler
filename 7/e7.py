#!/usr/bin/env python

from factorization.primegen import primegen

def main():
	# from http://en.wikipedia.org/wiki/Prime_number_theorem#Table_of_.CF.80.28x.29.2C_x_.2F_ln_x.2C_and_li.28x.29,
	# we see that 10^6 has just slightly less than 10k primes.
	# so start by generating primes < 2 mil; see if that's enough
	primes = list(primegen(2000000))
	try:
		result = primes[10000]
	except IndexError:
		print('too few primes')
		return
	print('10001st prime = {0}'.format(result))

if __name__ == '__main__':
	main()