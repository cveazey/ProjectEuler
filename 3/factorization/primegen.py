import itertools

def primegen(upper):
	"""Return all primes less than upper
	>>> primegen(10)
	[2, 3, 5, 7]
	>>> primegen(30)
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
	"""
	ls = [i for i in range(2,upper)]
	marked = [False] * len(ls)
	# START: p_idx = first false index in marked
	# if p_idx out of bounds, stop
	# p = ls[p_idx]
	# cursor = p + p
	# while cursor < upper: set marked[cursor - 2] to 1
	# goto START
	def next_p():
		for i,v in enumerate(marked):
			if not v:	
				yield i

	for p_idx in next_p():
		p = ls[p_idx]
		cursor = p
		while True:
			cursor = cursor + p
			try:
				marked[cursor-2] = True
			except IndexError:
				break

	inverted_marked = map(lambda x: not x, marked)
	primes = [p for p in itertools.compress(ls, inverted_marked)]
	return primes

if __name__ == '__main__':
	import doctest
	doctest.testmod()