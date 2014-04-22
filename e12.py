#!/usr/bin/env python -tt -Wall

import itertools
from collections import Counter
from factorization.factors import factors

def triangle(n):
	return sum(range(n+1))

def divisors(n):
	# return number of divisors of n
	c = Counter(factors(n))
	tally = 1
	for tpl in c.items():
		tally =  tally * (tpl[1] + 1)
	return tally

def first_triangle(num_divisors):
	n = 0
	d = 0
	while d <= num_divisors:
		n = n+1
		t = triangle(n)
		d = divisors(t)
	return (t,d,n)

def main():
	print first_triangle(500)

if __name__ == '__main__':
	main()