#!/usr/bin/env python

def collatz(start):
	r = [start]
	while (r[-1] > 1):
		n = r[-1]
		if ((n % 2) == 0):
			n = n/2
		else:
			n = (3 * n) + 1
		r += [n]
	return r

def longest_collatz(top):
	longest = []
	for i in xrange(top,0,-1):
		seq = collatz(i)
		if (len(seq) > len(longest)):
			longest = seq
	return longest

def main():
	longest = longest_collatz(1000000)
	print longest
	print len(longest)

if __name__ == '__main__':
	main()
