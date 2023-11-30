"""
Created on Thu 30 nov 2023 09:49:15 WET

@author: ChatGPT (prompt: "Write a Python function merge(xs, ys) to merge 
sorted lists xs and ys. Return a sorted result.")
"""
def merge(xs, ys):
    result = []
    i = j = 0
    while i < len(xs) and j < len(ys):
        if xs[i] < ys[j]:
            result.append(xs[i])
            i += 1
        else:
            result.append(ys[j])
            j += 1

    # Add the remaining elements from both lists, if any
    result.extend(xs[i:])
    result.extend(ys[j:])

    return result
