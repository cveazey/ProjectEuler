#!/usr/bin/env python

import itertools

def fib(upper):
	seq = [1, 1]
	while True:
		next = seq[-2] + seq[-1]
		if next > upper:
			break
		seq.append(next)
	return seq

def main():
	s = sum(itertools.ifilterfalse(lambda x: x%2, fib(4000000)))
	print('sum is {0}'.format(s))

if __name__ == '__main__':
	main()