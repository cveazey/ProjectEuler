import itertools

def primegen(upper):
	"""Return generator yielding all primes less than upper 
	>>> [p for p in primegen(10)]
	[2, 3, 5, 7]
	>>> [p for p in primegen(30)]
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
	"""
	marked = [False] * (upper - 2)
	
	# using generator here lets us lazily evaluate whether
	# a number has been marked
	def next_p():
		for i,v in enumerate(marked):
			if not v:
				yield i

	def generate_primes():
		for p_idx in next_p():
			p = p_idx + 2
			cursor = p
			while True:
				cursor = cursor + p
				try:
					marked[cursor-2] = True
				except IndexError:
					break
			yield p

	return generate_primes()

if __name__ == '__main__':
	import doctest
	doctest.testmod()