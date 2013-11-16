#!/usr/bin/env python

from factorization.factors import factors

def main():
	n = 600851475143
	f = factors(n)
	largest = f[-1]
	print('largest = {0}'.format(largest))
	
if __name__ == '__main__':
	main()