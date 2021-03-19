import base64

f = open('./peserta/flag.enc', 'r')
data = f.read()

dec = base64.b64decode(data)
for i in range(255):
    res = ""
    for j in dec:
        res += chr(ord(j) ^ i)
    if "LKS2021" in res:
        print res
        break