from pwn import *

with open('flag.enc', 'rb') as f:
  content = f.read()

for i in range(255):
  res = xor(content, i)
  if 'LKS2021' in res:
     print(res)
