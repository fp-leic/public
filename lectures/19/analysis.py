# -*- coding: utf-8 -*-
"""
NB19 : Analysis

pbv, jlopes
""" 
# ------------------------------------------------------------
# compute T(n) for this example function 
# (doesn't compute anything useful)
# ------------------------------------------------------------

def function(n):
a=5   # + 1
b=6   # + 1
c=0   # + 1
for i in range(n):  # n*.... 
    for j in range(n):  # n*....
          x = i * i     # +1 
          y = j * j     # +1
          z = i * j     # +1
for k in range(n):  # n*... 
    w = a*k + 45    # +1
    v = b*b         # +1
d = 33   # +1

# T(n) = 1+1+1 + n*(n*(1+1+1)) + n*(1+1) + 1
#       =  4 + 3*n^2 + 2*n
#       = 3*n^2 + 2*n + 4
#       = O(n^2) 


# ----------------------------------------
# Compute T(n) for this program that reverses a base-10 number
# ----------------------------------------------------------

n = int(input())  # +1
r = 0             # +1
while n>0:       # log(n,10)* ....
    r = 10*r + (n%10) # +1
    n = n // 10       # +1
print(r)  # +1

# T(n) = 2 + log(n,10) * 2 +1
#      = 3 + 2*log(n,10)
#      = 3 + (2/log(10)) * log(n)
#      = O(log(n))






