#!/usr/bin/python2

from random import randint
import string
import sys

LOWERS = string.ascii_lowercase
UPPERS = string.ascii_uppercase
DIGITS = string.digits

def shifting(char, shift):
    if char in LOWERS:
        index = LOWERS
    elif char in UPPERS:
        index = UPPERS
    elif char in DIGITS:
        index = DIGITS
    else:
        return char

    pos = index.index(char) + shift
    return index[-(abs(pos) % len(index))] if pos < 0 \
        else index[pos % len(index)]

def encode(text, shift):
    return ''.join(shifting(_, shift) for _ in text)
        

if __name__ == "__main__":
    flag = '<REDACTED>'

    if len(sys.argv) != 2:
        print('Usage: ./chall.py [TEXT]')
    else:
        stdin = sys.argv[1]
        encoded = encode(stdin, randint(1, 26))
        print(encoded)