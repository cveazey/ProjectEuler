#!/usr/bin/env python

from factorization.factors import factors

def smallest_multiple(n):
	"""Returns smallest multiple evenly divisble by each 1..n in N

	>>> smallest_multiple(10)
	2520

	"""

	# for each number <= n, find its prime factors p1^k1, p2^k2, ...
	# 	store as prime => exponent
	# 		replace existing stored exponents only if the replacement is greater
	# for each prime=>exponent
	# 	result = result * prime^exponent
	factor_exp_map = {}
	for i in xrange(n,0,-1):
		facs = list(factors(i))
		for factor in facs:
			fact_count = facs.count(factor)
			cur_fact_count = factor_exp_map.get(factor,0)
			if (fact_count > cur_fact_count):
				factor_exp_map[factor] = fact_count
	result = 1
	for factor, exponent in factor_exp_map.iteritems():
		result = result * factor**exponent
	return result

def main():
	print('result = {0}'.format(smallest_multiple(20)))
	
if __name__ == '__main__':
	main()