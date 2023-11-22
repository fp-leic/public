
# ------------------------------------------------------
# Lecture 17 - Effect free programming
# ------------------------------------------------------

# Modifiers vs. pure functions

def double_modifier(values):
    '''Double every value in a list.'''
    for i,v in enumerate(values):
        values[i] = 2*v
    # returns None

def double_pure(values):
    '''Double every value in a list.'''
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



# --------------------------------------------------
# Assert
# State conditions that should hold at a specific point 
# in the program
# --------------------------------------------------
def average(lst):
    # pre-condition for the function
    assert type(lst) is list and len(lst)>0, "argument should be non-empty list"
    return sum(lst) / len(lst)
            
