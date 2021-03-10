from z3 import *

s = Solver()
char = [Int('char%s' % (i)) for i in range(25)]

s.add(char[15] % char[5] == 5)
s.add(char[0] + char[21] == 218)
s.add(char[11] % char[14] - char[17] == -117)
s.add(char[7] + char[10] == 227)
s.add(char[24] * char[20] == 5610)
s.add(char[19] + char[13] - char[1] == 41)
s.add(char[6] - char[16] == 0)
s.add(char[18] - char[22] * char[23] == -11475)
s.add(char[9] - char[2] == 6)
s.add(char[8] % char[4] + char[3] == 164)
s.add(char[12] == 114)
s.add(char[14] - char[19] + char[8] == 102)
s.add(char[12] % char[20] + char[22] == 99)
s.add(char[7] + char[15] % char[10] == 219)
s.add(char[6] + char[17] == 212)
s.add(char[5] * char[3] == 5712)
s.add(char[9] * char[16] % char[0] == 0)
s.add(char[4] - char[11] == 9)
s.add(char[21] - char[18] == -12)
s.add(char[24] + char[13] - char[2] == 39)
s.add(char[23] % char[1] == 17)
s.add(char[5] + char[4] == 159)
s.add(char[9] * char[3] % char[21] == 5)
s.add(char[6] + char[11] % char[2] == 194)
s.add(char[20] + char[1] == 215)
s.add(char[22] - char[19] == 46)
s.add(char[23] - char[7] == 10)
s.add(char[0] * char[18] == 13225)
s.add(char[13] * char[10] == 11155)
s.add(char[24] % char[17] == 51)
s.add(char[12] + char[14] == 213)
s.add(char[16] - char[8] == 43)
s.add(char[15] == 107)


if s.check() == sat:
    m = s.model()
    chars = ''
    for c in char:
        chars += chr(m[c].as_long())

    print chars