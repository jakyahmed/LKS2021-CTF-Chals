import base64

flag = "LKS2021{ez_xor_crypto}"
key  = "f"
res = ""

for i in flag:
    res += chr(ord(i) ^ ord(key))

f = open('./peserta/flag.enc', 'w')
f.write(base64.b64encode(res))