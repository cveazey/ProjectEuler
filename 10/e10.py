#!/usr/bin/env python -tt -Wall

def prime_sieve(upper):
	marked = [False] * (upper-2)

	def next_prime():
		for i,v in enumerate(marked):
			if not v:
				yield i+2

	next_prime_gen = next_prime()
	for p in next_prime_gen:
		for n in xrange(2*p - 2, len(marked), p):
			marked[n] = True
		yield p

def main():
	print(sum(list(prime_sieve(2000000))))

if __name__ == '__main__':
	main()