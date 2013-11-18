#!/usr/bin/env python

def sum_seq_squares(n):
    return (n * (n+1) * ((2*n)+1)) / 6

def sum_seq(n):
    return (n * (n + 1)) / 2

def main():
	sum_seq_sq_100 = sum_seq_squares(100)
	sum_seq_100 = sum_seq(100)
	sq_sum_seq_100 = sum_seq_100**2
	diff = sq_sum_seq_100 - sum_seq_sq_100
	print('diff is {0}'.format(diff))

if __name__ == '__main__':
	main()