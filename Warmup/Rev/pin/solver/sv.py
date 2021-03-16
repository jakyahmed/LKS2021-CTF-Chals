from z3 import *

s = Solver()
char = [Int('char%s' % (i)) for i in range(6)]

s.add(char[0] + char[5] == 109)
s.add(char[4] - char[1] % char[3] == 5)
s.add(char[2] == 50)
s.add(char[5] + char[4] % char[0] == 58)
s.add(char[2] + char[3] == 105)
s.add(char[1] == 48)
s.add(char[2] + char[0] == 102)
s.add(char[3] - char[1] == 7)
s.add(char[4] % char[5] == 53)
s.add(char[4] - char[3] * char[2] == -2697)
s.add(char[5] + char[0] == 109)
s.add(char[1] == 48)
s.add(char[2] % char[5] == 50)
s.add(char[3] + char[0] == 107)
s.add(char[1] % char[4] == 48)

if s.check() == sat:
    m = s.model()
    chars = ''
    for c in char:
        chars += chr(m[c].as_long())

    print chars