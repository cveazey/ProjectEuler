#!/usr/bin/env python

from factorization.factors import factors

def main():
	n = 600851475143
	largest = 0
	for p in factors(n):
		largest = p
	print('largest = {0}'.format(largest))

if __name__ == '__main__':
	main()