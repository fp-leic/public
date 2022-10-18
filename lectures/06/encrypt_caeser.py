#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 00:26:39 2022

@author: jlopes
"""


def encrypt(text, shift):
    """Encrypt text using Caeser of s."""
    result = ""

    # transverse the plain text

    # for i in range(len(text)):
    #     char = text[i]

    for char in text:

        # Encrypt uppercase characters in plain text
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
        
            # result += chr((ord(char) - 65 + shift) % 26 + 65)

        # Encrypt lowercase characters in plain text
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