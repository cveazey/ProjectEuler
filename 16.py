#!/usr/bin/env python

import misc

def main():
	check = misc.digit_sum(2**15)
	print('2**15 digit sum = {}'.format(check))
	result = misc.digit_sum(2**1000)
	print('2**1000 digit_sum = {}'.format(result))

if __name__ == '__main__':
	main()