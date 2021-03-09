#!/usr/bin/python3

from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from sys import stdout

import base64
import os

class Unbuffered(object):
	def __init__(self, stream):
		self.stream = stream
	def write(self, data):
		self.stream.write(data)
		self.stream.flush()
	def writelines(self, datas):
		self.stream.writelines(datas)
		self.stream.flush()
	def __getattr__(self, attr):
		return getattr(self.stream, attr)

stdout = Unbuffered(stdout)
flag = os.environ.get('SECRET_FLAG')
iv = bytes(os.environ.get('IV'), 'utf-8')
key = os.urandom(16)

def prompt():
    print("""\n
1. Read file
2. Check flag
    """)

    try:
        choice = int(input('Option: '))

        if choice == 1:
            args = input('Path: ')
            read_file(args)
        elif choice == 2:
            args = input('Flag: ')
            check_flag(args)

    except Exception:
        pass

def encrypt(text):
    aes = AES.new(key, AES.MODE_OFB, iv)
    enc = aes.encrypt(pad(text, 16))

    return base64.b64encode(enc)

def read_file(filename):
    if os.path.isfile(filename):
        with open(filename, 'rb') as handle:
            content = handle.read()
        
        encrypted = encrypt(content)
        stdout.write(encrypted.decode())

def check_flag(text):
    if text == flag:
        stdout.write('Correct')
    else:
        stdout.write('Incorrect')

if __name__ == '__main__':
    while True:
        prompt()