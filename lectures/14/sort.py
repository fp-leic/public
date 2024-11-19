"""
# -*- coding: utf-8 -*-
Created on Mon Dec  3 19:58:14 2018

@author: jlopes
"""

job_data = [
   ('121', 'Yates', 'NY', 5094),
   ('122', 'Wyoming', 'NY', 8722),
   ('001', 'Albany', 'NY', 162692),
   ('003', 'Allegany', 'NY', 11986),
   ]

print()
print(job_data)

# standard sort
sorted_data = sorted(job_data)
print()
print(sorted_data)

# sort by key
def by_state(a):
    return a[1]

key_sorted_data = sorted(job_data,key=by_state)
print()
print(key_sorted_data)
