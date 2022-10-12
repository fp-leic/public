#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:48:55 2022

@author: jlopes
"""

"""Python function to check if a number is palindrome or not.

Definition of palindrome: a word, verse, or sentence (such as
"Able was I ere I saw Elba") or a number (such as 1881)
that reads the same backward or forward
"""


def reverse_number(number):
    reverse = 0
    while number != 0:
        last = number % 10
        reverse = reverse * 10 + last
        number = number // 10
    return reverse


print(reverse_number(1234))
print(reverse_number(3443))
print(reverse_number(1234567))


def palindrome_check(number):
    reverse = reverse_number(number)

    if(reverse == number):
        print(number, "is a palindrome number")
    else:
        print(number, "is not a palindrome number")


palindrome_check(131)
palindrome_check(3443)
palindrome_check(1234567)