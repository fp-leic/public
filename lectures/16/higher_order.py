# --------------------------------------------
# Lecture 16 - Higher order functions
# --------------------------------------------
# Pedro Vasconcelos, 2022
#

#
# Sum squares of numbers from 1 to n
#
def sum_squares(n):
    total = 0
    for i in range(1,n+1):
        total = total + i**2
    return total

#
# Sum cubes of numbers from 1 to n
#
def sum_cubes(n):
    total = 0
    for i in range(1, n+1):
        total = total + i**3
    return total

# Common pattern:
# Summation as a higher-order function
#
def summation(n, term):
    total = 0
    for i in range(1, n+1):
        total = total + term(i)
    return total

#
# Sum_squares and sum_cubes are special cases of summation
#
def sum_squares2(n):
    return summation(n, lambda x:x*x)

def sum_cubes2(n):
    return summation(n, lambda x: x*x*x)

print(sum_squares(10), sum_squares2(10))
print(sum_cubes(10), sum_cubes2(10))


#
# Summation is a special case of sum, map and range
#
def sum_squares3(n):
    return sum(map(lambda x:x*x, range(1,n+1)))


# ------------------------------------------------
# Utilities
# ------------------------------------------------
import functools

#----------------------------------------------
# Composition: pipeline several functions together
#-----------------------------------------------
def compose(*args):
    def inner(x):
        for fun in reversed(args):
            x = fun(x)
        return x
    return inner
   
fog = compose(lambda x:3*x, lambda x:x+1)
#                 ^----f        ^------g
# f(g(2)) = 3*(2+1) = 9
print(fog(2)) 

# -------------------------------------------------------------
# Partial application: define some arguments of the function
# ------------------------------------------------------------
def example(x,y):
    return 3*x+y

example5 = functools.partial(example, 5) # fix the first argument
print(example5(2)) # equals example(5,2)


# --------------------------------------------------------------------
# Currying: transform a function to take one argument at a time
# ------------------------------------------------------------------
def curried_example(x):
    def inner(y):
        return 3*x+y
    return inner

print(curried_example(5)(2))

# We can simply apply curried function to obtain partial application
curried_example5 = curried_example(5)
print(curried_example5(2)) # equals example(5,2)

# ----------------------------------------------------------------
# Combining functions
# Using compose and functools.partial above
# ----------------------------------------------------------------

# First the individuals functions

# Break a string into a list of words
def break_words(str):
    """Break a string into a list of words."""
    return str.split()

def join_words(alist):
    """Join a list of words together."""
    return ' '.join(alist)

# Filter out short words, i.e. less then 3 characters
def remove_short(words):
    return filter(lambda w:len(w)>=3, words)

# we could also define this using functools.partial
# remove_short = functools.partial(filter, lambda w : len(w)>=3)


# 
# A processing pipeline. Given a string:
# - break it in a list of words
# - remove all words with less than 3 characters
# - join the words together

process = compose(join_words, remove_short, break_words)
print(process("It was the best of times, it was the worst of times"))



# ----------------------------------------------
# Closures
# -----------------------------------------------

#
# Naive recursive Fibonacci
# Warning: this is slow; try to compute fib(35)
#
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2) 


# A higher-order function that 
# return a "memorized" version of a function
# i.e. one that stores results to avoid re-computations
def memorize(function):
    memo = dict()      # empty dictionary for results
    def wrapper(arg):
        if arg in memo:
            print(f'returning memorized argument: {arg} -> {memo[arg]}')
            return memo[arg]
        else:
            print(f'computing argument {arg} for the first time')
            result = function(arg)
            memo[arg] = result
            return result
    return wrapper   # no parenthesis


# Fibonnacci with memorized results

fibmemo = memorize(fib)

# The first call is slow, but the second call is instantaneous
print(fibmemo(30))
print(fibmemo(30))

# NB: the memoized recursive definition of NB12 is still faster; why?

