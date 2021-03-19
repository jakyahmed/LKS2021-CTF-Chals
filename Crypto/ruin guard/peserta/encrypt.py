plain = "this_is_absolutely_not_the_flag"

mapper = {
    '0': '.',
    '1': '2',
    '2': '3'
}

def encoder(n):
    result = ""
    while n > 0:
        m = int(n % 3)
        result += mapper[str(m)]
        n //= 3

    result = result[::-1]
    return result

cipher = ""
for i in plain:
    cipher += encoder(ord(i))
    cipher += '-'

print(cipher)