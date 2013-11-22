#!/usr/bin/env python -tt -Wall

import operator
import itertools

def entry(grid,r,c):
	if r<0 or c<0:
		return 0
	try:
		return grid[r][c]
	except IndexError:
		return 0

def run(grid,r,c,d):
	return (entry(grid, r+dr, c+dc) for dr,dc in d)

def main():
	south = ((0,0), (1,0), (2,0), (3,0))
	southeast = ((0,0), (1,1), (2,2), (3,3))
	east = ((0,0), (0,1), (0,2), (0,3))
	northeast = ((0,0), (-1,1), (-2,2), (-3,3))
	with open('input', 'r') as f:
		grid = [[int(e) for e in l.split()] for l in f]
	dirs = (south,southeast,east,northeast)
	height = xrange(len(grid))
	width = xrange(len(grid[0]))
	iterator = itertools.product(height,width,dirs)
	products = (reduce(operator.mul,run(grid,r,c,d)) for r,c,d in iterator)
	print max(products)  # 70600674

if __name__ == '__main__':
	main()