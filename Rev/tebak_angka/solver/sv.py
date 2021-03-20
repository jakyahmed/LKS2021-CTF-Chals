from pwn import *
from ctypes import CDLL
from math import floor

import time

con = remote('localhost', 30002, level='error')
libc = CDLL('libc-2.31.so')
now = int(floor(time.time()))

libc.srand(now)
number = str(libc.rand())
con.sendline(number)
print(con.recvall())