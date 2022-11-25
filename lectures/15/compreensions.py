#
# Lecture 15 - Compreensions and generators
#
# Pedro Vasconcelos, 2022
#

# -------------------------------------------------------
# List compreensions
# -------------------------------------------------------

# Naive prime test
def is_prime(n):
    """Test if an integer n is prime."""
    # list all proper divisors i.e. between 2 and n-1
    divisors = [d for d in range(2,n) if n%d == 0]
    # n is prime iff n>1 and has no proper divisors
    return n>1 and len(divisors) == 0


# List all prime upto n (inefficiently)
def primes_upto(n):
    return [p for p in range(2,n) if prime(p)]

# Pythagorean triples
def pythagorean_triples(n):
    """List all triples (x,y,z) such that x**2+y**2==z**2 and x,y,z < n."""
    return [(x,y,z)
            for x in range(1,n)
            for y in range(1,n)
            for z in range(1,n)
            if x**2+y**2==z**2]

# nested for compreensions are similar to nested for loops:
def pythagorean_imperative(n):
    for x in range(1,n):
        for y in range(1,n):
            for z in range(1,n):
                if x**2+y**2==z**2:
                    print((x,y,z))


# Construct the identity matrix of dimensions n*n
def identity_matrix(n):
    return [[int(row==col) for col in range(n)] for row in range(n)]


# ------------------------------------------------------------------
# Generators
# ------------------------------------------------------------------
import math
import itertools

#
# A generator for the infinite sequece of terms of the cosine series
# cos(x) = 1 - x^2/2! + x^4/4! + ... + x^(2n)/(2n)! + ...
#
# itertools.count(0) is a generator for 0, 1, 2, ...
def gen_cosine(x):
    terms = ((-1)**n*x**(2*n)/math.factorial(2*n) for n in itertools.count(0))
    return terms

def approx_cosine(x, n):
    """Approximate cosine taking n terms from the series above."""
    terms = gen_cosine(x)
    # itertools.slice(term, n) takes the first n elements from a generator
    result = sum(itertools.islice(terms, n))
    return result


# -----------------------------------------------------------------
# Set comprehensions
# -----------------------------------------------------------------
from math import sqrt

# Compute the set of primes upto a given number
#
# Using the *sieve of Erathostenes*:
# 1) generate all compositive numbers upto n, i.e., numbers of the form
#   i*2, i*3, .... such that i <= sqrt(n)
# 2) remove the compositive numbers from the set of all number {1,...n}
#
def primes_upto(n):
    sqrt_n = int(sqrt(n))
    composites = {j for i in range(2, sqrt_n + 1) for j in range(i*2, n, i)}
    primes = {p for p in range(2, n) if p not in composites}
    return primes 

