#!/usr/bin/env python2

def validate_pin(char):

    if (char[0] + char[5] != 109):
        return False
    if (char[4] - char[1] % char[3] != 5):
        return False
    if (char[2] != 50):
        return False
    if (char[5] + char[4] % char[0] != 58):
        return False
    if (char[2] + char[3] != 105):
        return False
    if (char[1] != 48):
        return False
    if (char[2] + char[0] != 102):
        return False
    if (char[3] - char[1] != 7):
        return False
    if (char[4] % char[5] != 53):
        return False
    if (char[4] - char[3] * char[2] != -2697):
        return False
    if (char[5] + char[0] != 109):
        return False
    if (char[1] != 48):
        return False
    if (char[2] % char[5] != 50):
        return False
    if (char[3] + char[0] != 107):
        return False
    if (char[1] % char[4] != 48):
        return False

    return True

if __name__ == '__main__':
    pin = raw_input('Enter pin: ')

    if len(pin) == 6:
        if validate_pin((map(ord, pin))):
            print('Correct Pin!')
            print('Flag: LKS2021{%s}' % (pin))
        else:
            print('Incorrect Pin!')
    else:
        print('Must be 6-digit pin')
    