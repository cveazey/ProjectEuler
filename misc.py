# def binomial_coefficient(n,k):
# 	c = 1
# 	for i in range(1,k+1):
# 		c = c * ( (n + 1 - i) / i)
# 	return c

from fractions import Fraction
from operator import mul

def binomial_coefficient(n,k):
    series = [Fraction(n+1-i,i) for i in range(1,k+1)]
    result = reduce(mul, series)
    return int(result)
    
# def binomial_coefficient(n,k):
#     if k < 0 or k > n:
#         return 0
#     if k == 0 or k == n:
#         return 1
#     k = min(k, n - k) # take advantage of symmetry
#     c = 1
#     for i in range(k):
#     	t1 = c
#     	t2 = (n - 1)
#     	t3 = i+1
#         c = t1 * t2 / t3
#         print('c = {}'.format(c))
#         print('t1 * t2 / t3 = {} * {} / {}'.format(t1,t2,t3))
#     return c
