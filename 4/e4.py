#!/usr/bin/env python

import itertools

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


def products(r1,r2):
	product = itertools.product(r1, r2)
	after_mult = map(lambda x: x[0] * x[1], product)
	after_sort = sorted(after_mult)
	return after_sort

def three_digit_products():
	return products(range(999,900,-1),range(999,900,-1))	

def two_digit_products():
	return products(range(99,90,-1),range(99,90,-1))

def larget_palindrome(numbers):
	"""Returns the last palindrome number in the iterable arg numbers
	
	>>> gen = two_digit_products()
	...
	>>> larget_palindrome(gen)
	9009

	"""
	for number in reversed(numbers):
		if is_int_palindrome(number):
			return number


def main():
	print('2 digits is {0}'.format(larget_palindrome(two_digit_products())))
	# print('3 digits is {0}'.format(larget_palindrome(three_digit_products())))

if __name__ == '__main__':
	main()