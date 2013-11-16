#!/usr/bin/env python

import bisect

def is_int_palindrome(num):
	"""Returns True if input is a palindrome number
	Otherwise returns False.

	>>> is_int_palindrome(1441)
	True
	>>> is_int_palindrome(1442)
	False
	>>> is_int_palindrome(144441)
	True
	>>> is_int_palindrome(144442)
	False

	Someday, maybe this will throw some exceptions!
	"""

	forward, backward = [], []
	while num > 0:
		least_sig_digit = num % 10
		forward = [least_sig_digit] + forward
		backward = backward + [least_sig_digit]
		num /= 10
	palindrome = forward == backward
	return palindrome


def three_digit_products():
	# """Generates products of three digit numbers, increasing order

	# >>> prods = three_digit_products()
	# ...
	# >>> prods[-1]
	# 998001
	# >>> prods[-2]
	# 997002

	# """

	result = []
	for i in xrange(999,99,-1):
		for j in xrange(i,99,-1):
			bisect.insort(result, i*j)
	return result
	

def gen_products_two_digits():
	result = []
	for i in xrange(99,9,-1):
		for j in xrange(i,9,-1):
			bisect.insort(result, i*j)
	return result


def larget_palindrome(numbers):
	"""Returns the last palindrome number in the iterable arg numbers
	
	>>> gen = gen_products_two_digits()
	...
	>>> larget_palindrome(gen)
	9009

	"""
	for number in reversed(numbers):
		if is_int_palindrome(number):
			return number


def main():
	result = larget_palindrome(three_digit_products())
	print('result is {0}'.format(result))

if __name__ == '__main__':
	main()