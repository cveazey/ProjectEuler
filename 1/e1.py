#!/usr/bin/env python

import itertools

def naive(upper):
	sum = 0
	for i in range(upper):
		if not i % 3 or not i % 5:
			sum = sum + i
	return sum	

def ifilterfalse_based(upper):
	return sum(itertools.ifilterfalse(lambda x: x%3 and x%5, range(upper)))

def list_comprehension_based(upper):
	mults = [num for num in range(upper) if not (num%3 and num%5)]
	return sum(mults)

def filter_based(upper):
	return sum(filter(lambda x: not (x%3 and x%5), range(upper)))

def generator_based(upper):
	def g(upper):
		for i in xrange(upper):
			if not i % 3 or not i % 5:
				yield i
	return sum(g(upper))

def main():
	upper = 1000
	sum = naive(upper)
	print('naive sum is ' + str(sum))
	sum = ifilterfalse_based(upper)
	print('ifilterfalse sum is {0}'.format(str(sum)))
	sum = list_comprehension_based(upper)
	print('list comp sum is {0}'.format(str(sum)))
	sum = filter_based(upper)
	print('filter sum is {0}'.format(str(sum)))
	sum = generator_based(upper)
	print('generator sum is {0}'.format(str(sum)))

if __name__ == '__main__':
	main()