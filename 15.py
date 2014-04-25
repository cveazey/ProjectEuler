#!/usr/bin/env python

from misc import binomial_coefficient as bc

def possible_lattice_paths(n):
	return bc(n+n,n)

def main():
	two = possible_lattice_paths(2)
	three = possible_lattice_paths(3)
	four = possible_lattice_paths(4)
	print('2x2 (should be 6): {}'.format(two))
	print('3x3: (should be 20) {}'.format(three))
	print('4x4: (should be 70) {}'.format(four))
	twenty = possible_lattice_paths(20)
	print('20x20: {}'.format(twenty))
	
if __name__ == '__main__':
	main()