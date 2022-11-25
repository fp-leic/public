#
# Lecture 14 - Map, filter and reduce
#
# Pedro Vasconcelos, 2022
#
#
import functools
import operator

# ------------------------------------------------------------
# Map
# ------------------------------------------------------------

def celsius_to_fahrenheit(degrees):
    "Convert temperature from Celsius to Fahrenheit degrees."
    return degrees*9/5+32

temperatures_celsius = [ 18, 19, 21, 22, 24, 24, 22, 22 ]

temperatures_fahrenheit = map(celsius_to_fahrenheit, temperatures_celsius)

# NB: iterator objects are "consumed" by using them
# second print yields an empty list
# print(list(temperatures_fahrenheit))
# print(list(temperatures_fahrenheit))


# --------------------------------------------------------
# Filter
# --------------------------------------------------------

def greater_than_70(degrees):
    return degrees > 70

filtered_temperatures = filter(greater_than_70, temperatures_fahrenheit)


# Lambdas

temperatures_fahrenheit = map(lambda degrees: degrees*9/5+32, temperatures_celsius)
filtered_temperatures = filter(lambda degrees: degrees>70, temperatures_fahrenheit)

# Average of the filtered temperatures:
# The following doesn't work:
# - filter object has no length
# - even if it did we can't use it twice!

# avg_temperature = sum(filtered_temperatures)/len(filtered_temperatures)

# But we can convert to a list:
list_temperatures = list(filtered_temperatures)
avg_temperature = sum(list_temperatures)/len(list_temperatures)

# --------------------------------------------------------------
# Reduce
# --------------------------------------------------------------

# We can compute the sum of all temperatures using reduce:
def add(a,b):
    return a+b

print(functools.reduce(add, list_temperatures, 0))

# same thing, using a lambda
print(functools.reduce(lambda a,b: a+b, list_temperatures, 0))

# same thing, using the operator module
print(functools.reduce(operator.add, list_temperatures, 0))

# We can also compute the product of all temperatures:
def mult(a,b):
    return a*b

print(functools.reduce(mult, list_temperatures, 1))
    
# same thing, using a lambda
print(functools.reduce(lambda a,b: a*b, list_temperatures, 1))

# same thing, using the operator module
print(functools.reduce(operator.mul, list_temperatures, 1))


# Compute factorial using reduce
def factorial(n):
    """Compute factorial of n using reduce."""
    return functools.reduce(mult, range(2,n+1), 1)

# Understanding reduce
# this function produces a string showing its arguments
def f(x,y):
    return "f(" + str(x) + "," + str(y) + ")"

# without initial value
print(functools.reduce(f, range(1,5)))
# gives "f(f(f(1,2),3),4)"

# with initial value 0
print(functools.reduce(f, range(1,5), 0))
# gives "f(f(f(f(0,1),2),3),4)"


# ------------------------------------------------------------------
# Compute the average in a single pass over the data
# ------------------------------------------------------------------
# in imperative style: using a loop

def average_imperative(alist):
    total = 0
    count = 0
    for value in alist:
        total += value
        count += 1
    return total / count

# in functional style: using functools.reduce
# first an auxiliary function
def add_value(pair, value):
    total, count = pair
    return (total+value, 1+count)

# now we use reduce to compute averages in one go
def average_functional(alist):
    total, count = functools.reduce(add_value, alist, (0,0))
    return total/count

# Example:
print(average_functional(map(celsius_to_fahrenheit, temperatures_celsius)))
      
