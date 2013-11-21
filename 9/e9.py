#!/usr/bin/env python -tt -Wall

import itertools

def main():
	k = 1000
	factors = [4, 25]
	ranges = (xrange(f, k/4, f) for f in factors)
	multiples = itertools.ifilter(lambda m: not k%(2*m), itertools.chain(*ranges))
	raw_pairs = itertools.imap(lambda m: (m, (k/(2*m)) - m), multiples)
	pairs = itertools.ifilter(lambda (m,n): m>n and n>0, raw_pairs)
	triplets = itertools.imap(lambda (m,n): (m**2 - n**2, 2 * m * n, m**2 + n**2),pairs)
	for a,b,c in triplets:
		print('a = {0}, b = {1}, c = {2}, a+b+c = {3}, abc = {4}'.format(a, b, c, a+b+c, a*b*c))

if __name__ == '__main__':
	main()