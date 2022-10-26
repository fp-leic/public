#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 01:08:23 2022

@author: jlopes
"""

"""
The rules for NIF validation are:
- Validate size (9 digits)
- The first digit has to be 1, 2, 3, 5, 6, 7, 8 or 9 (2 and 3 added later)
- The checksum is given by 9xd1 + 8xd2 + 7xd3 + ... + 3xd7 + 2xd8
- If remainder of the division by 11 is less than 2, check digit is 0
- Otherwise it's 11 minus the remainder
- The NIF is valid if d9 is equal to the check_digit
"""


def validate_NIF(nif):
    MAX = 9
    MIN_NIF = 10**(MAX-1)  # 100000000
    VALID_FIRSTS = [1, 2, 3, 5, 6, 7, 8, 9]

    if nif < MIN_NIF:
        return f'{nif} is not a valid NIF: too short'

    first = nif // MIN_NIF
    if first not in VALID_FIRSTS:
        return f'{nif} is not a valid NIF: {first} is not a first'

    # get the right most digit
    d9 = nif % 10
    n = nif // 10

    # calculate the checksum according to the formula
    checksum = 0
    for i in range(2, MAX+1):
        d = n % 10
        checksum += i*d
        n = n // 10

    # calculate the check digit
    rem = checksum % 11
    if rem < 2:
        checkdigit = 0
    else:
        checkdigit = 11 - rem

    # check d9
    if d9 == checkdigit:
        return f'{nif} is a valid NIF'
    else:
        return f'{nif} is not a valid NIF: {checkdigit} is not {d9}'

# drive code
print()
print(validate_NIF(12345678))
print(validate_NIF(123456789))
print(validate_NIF(342345678))
print(validate_NIF(134114025))
print(validate_NIF(152114025))
