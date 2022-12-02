# --------------------------------------------
# Lecture 16 - Higher order functions
# --------------------------------------------

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


# ------------------------------------------------
# Utilities
# ------------------------------------------------
import functools

#------------------------------------------
# Composition: pipeline two functions together
#-----------------------------------------
def compose(f,g):
    def inner(x):
        return f(g(x))
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
def into_words(str):
    return str.split()

# Filter out short words, i.e. less then 3 characters
remove_short = functools.partial(filter, lambda w:len(w)>=3)

# Join together a sequence of words
def join_together(words):
    return ' '.join(words)

# 
# Given a string:
# - break it in a list of words
# - remove all words with less than 3 characters
# - join the words together
#
combination = compose(compose(join_together, remove_short), into_words)

print(combination("a mary had my little lamb"))


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


# A Higher-order function that 
# return a "memorized" version of a function
# i.e. stores function results to avoid re-computations
def memorize(function):
    memo = dict()              # empty dictionary for results
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

fast_fib = memorize(fib)

# The first call is slow, but the second call is instantaneous

print(fast_fib(35))
print(fast_fib(35))
