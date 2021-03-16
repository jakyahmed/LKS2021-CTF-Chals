import string

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

def decode(text, shift):
    shift *= -1
    return ''.join(shifting(_, shift) for _ in text)

encoded = 'JIQ6465{hs9r_8_qgknj7_a8c9yp_a5nfcp}'
for enum in range(26):
    decoded = decode(encoded, enum)
    
    if 'LKS2021' in decoded:
        print '{:<2} {}'.format(enum, decoded)