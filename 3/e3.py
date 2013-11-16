#!/usr/bin/env python

from factorization.factors import factors

def main():
	n = 600851475143
	largest = [p for p in factors(n)][-1]
	print('largest = {0}'.format(largest))

if __name__ == '__main__':
	main()