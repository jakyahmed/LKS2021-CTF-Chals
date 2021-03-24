cipher_filename = "encrypted_message.txt"

mapper = {
    '.': '0',
    '2': '1',
    '3': '2'
}

cipher_data = open(cipher_filename, 'r').read()
cipher_list = cipher_data.split('-')

# convert from N base to decimal (10 base)
# SUM i=0 to N (base ** i) * x
def decoder(base, cipher):
    ascii_data = 0
    i = 0
    cipher = cipher[::-1] # reverse
    for x in cipher:
        ascii_data += ((base ** i) * int(mapper[x]))
        i += 1
    return chr(ascii_data)

plain = ""
for cipher in cipher_list:
    plain += decoder(3, cipher) # base 3 to decimal
print(plain)