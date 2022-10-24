#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 23:08:23 2022

@author: jlopes
"""

"""
The rules for NIF validation are:
- Validate size (9 digits)
- The first digit has to be 1, 2, 5, 6, 7, 8 or 9
- The checksum is given by 9xd1 + 8xd2 + 7xd3 + ... + 3xd7 + 2xd8
- If remainder of the division by 11 is less than 2, check digit is 0
- Otherwise it's 11 minus the remainder
- The NIF is valid if d9 is equal to the check_digit
"""


def validate_NIF(nif):
    nif = str(nif)  # convert to string if needed

    MAX = 9
    VALID_FIRSTS = [1, 2, 5, 6, 7, 8, 9]

    if len(nif) < MAX:
        return f'{nif} is not a valid NIF: too short'

    first = int(nif[0])
    if first not in VALID_FIRSTS:
        return f'{nif} is not a valid NIF: {first} is not a first'

    # get the right most digit
    d9 = int(nif[MAX-1])

    # calculate the checksum according to the formula
    checksum = 0
    for i in range(0, MAX-1):
        d = int(nif[i])
        # print(MAX-i, d)
        checksum += (MAX-i)*d
    # print(checksum)

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
print(validate_NIF(342345678))
print(validate_NIF(134114025))
print(validate_NIF(152114025))
