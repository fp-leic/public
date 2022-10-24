#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 00:26:39 2022

@author: jlopes
"""

"""
PROBLEM 6 (Caesar cipher):

Write a function to encrypt text using the Caeser cipher.

In cryptography, a Caesar cipher, also known as Caesar's cipher, the
shift cipher, Caesar's code or Caesar shift, is one of the simplest
and most widely known encryption techniques.
It is a type of substitution cipher in which each letter in the
plaintext is replaced by a letter some fixed number of positions
down the alphabet.
For example, with a left shift of 3, D would be replaced by A, E 
would become B, and so on. 
The method is named after Julius Caesar, who used it in his 
private correspondence.
https://en.wikipedia.org/wiki/Caesar_cipher

The ASCII table: https://en.cppreference.com/w/cpp/language/ascii
"""

def encrypt(text, shift):
    """Encrypt text using Caeser of 'shift'."""

    result = ""

    # transverse the plain text

    # for i in range(len(text)):
    #     char = text[i]
    for char in text:

        # encrypt uppercase characters in plain text
        if (char.isupper()):
            # ord('A') => 65; chr(65) => 'A'
            # there are 26 letters

            # find the position in 0-25
            index = ord(char) - ord('A')

            # perform the shift
            new_index = (index + shift) % 26

            # convert to new character
            new_unicode = new_index + ord('A')

            new_character = chr(new_unicode)

            # append to encrypted string
            result += new_character

            # in one line!
            # result += chr((ord(char) - 65 + shift) % 26 + 65)

        # encrypt lowercase characters in plain text
        else:
            # ord('a') => 97; chr(97) => 'a'

            result += chr((ord(char) - 97 + s) % 26 + 97)
    return result


# check the above function
text = "CEASER CIPHER DEMO"
s = 4

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + encrypt(text, s))