
# ------------------------------------------------------
# Lecture 17 - Effect free programming
# ------------------------------------------------------

# Modifiers vs. pure functions
# Modifiers : + re-uses space
# Pure : - requires more space
#      : + can acccess the previous values

def double_modifier(values):
    for i,v in enumerate(values):
        values[i] = 2*v
    # returns None

def double_pure(values):
    return [2*v for v in values]

#
# An issue with modifiers:
# Watch out for *iterator invalidation*, i.e.,
# removing or adding elements to a collection we are iterating over
#
def remove_evens_modifier(values):
    for value in values:
        if value%2 == 0:
            values.remove(value)  # WRONG!
    
values = [1,2,2,3,4]
remove_evens_modifier(values)
print(values)   # does not give the expected result!

# No iterator invalidation with the pure function
def remove_evens_pure(values):
    return [v for v in values if v%2!=0]

values = [1,2,2,3,4]
values = remove_evens_pure(values)
print(values)   # gives the expected result


# --------------------------------------------------------
# Avoiding control flow
# -------------------------------------------------------
def pythagorean_imperative(n):
    """Collect the list of all pythagorean triples x,y,z < n."""
    result = []
    for x in range(1,n):
        for y in range(1,n):
            for z in range(1, n):
                if x**2+y**2==z**2:
                    result.append((x,y,z))
    return result

def pythagorean_functional(n):
    result = [(x,y,z) for x in range(1,n)
              for y in range(1,n)
              for z in range(1,n)
              if x**2+y**2==z**2]
    return result

# ----------------------------------------------------
# Recursive Quicksort
# ----------------------------------------------------

def quicksort(lst):
    """Sort a list using the QuickSort algorithm."""
    if len(lst) == 0:    # Base case: empty list
        print('base case: quicksort([])')
        return []
    else:
        # Recursive case: list has at least one element
        pivot = len(lst) // 2
        smaller = [v for v in lst if v < lst[pivot]]
        pivots = [v for v in lst if v == lst[pivot]]
        larger = [v for v in lst if v > lst[pivot]]
        print(f'quicksort({smaller}) + {pivots} + quicksort({larger})')
        return quicksort(smaller) + pivots + quicksort(larger)


# -------------------------------------------------------
# Generator functions
# -------------------------------------------------------

# Generate all squares of natural numbers less than n
def gen_squares_less_than(number):
    for i in range(1, number):
        yield i**2
    
# for x in gen_squares_less_than(10):
#    print(x)

# Generate the infinite sequence n, n+1, n+2, .... 
def count(n):
    while True:
        yield n
        n = n + 1


# Generate the infinity sequence of all prime numbers
def get_primes():
    candidate = 2
    found = []
    while True:
        if all(candidate % prime != 0 for prime in found):
            yield candidate
            found.append(candidate)
        candidate += 1

# Print a table of all primes < 100
# zip combines two sequences into a sequence of pairs
# e.g. zip([1,2,3,4], "abcd")
# yields (1,'a'), (2,'b'), (3,'c'), (4,'d')
# -----------------------------------
for n, prime in zip(count(1),get_primes()):
    if prime>100:
        break
    print(f'prime number {n} is {prime}')
    
# --------------------------------------------------
# Assert
# State conditions that should hold at a specific point 
# in the program
# --------------------------------------------------
def average(lst):
    # pre-condition for the function
    assert type(lst) is list and len(lst)>0, "argument should be non-empty list"
    return sum(lst) / len(lst)
            
