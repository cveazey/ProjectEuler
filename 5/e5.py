#!/usr/bin/env python


def gcd(a,b):
	"""Returns the greatest common divisor of a and b

	>>> gcd(100,90)
	10
	>>> gcd(1000,750)
	250

	"""
	while b:
		a, b = b, a % b
	return a

def lcm(a,b):
	"""Returns least common multiple of a and b
	a and b being pos integers
	>>> lcm(12,58)
	348
	>>> lcm(10,14)
	70
	"""
	numerator = a*b
	denominator = gcd(a,b)
	return numerator / denominator
	
def lcm_series(n):
	"""Returns lcm of each 1..n

	>>> lcm_series(10)
	2520
	>>> lcm_series(20)
	232792560

	"""
	if n == 1:
		return n
	return lcm(n,lcm_series(n-1))

def main():
	print('result = {0}'.format(lcm_series(20)))
	
if __name__ == '__main__':
	main()