## Judul Soal
pin

## Deskripsi Soal

---
## Proof of Concept
- Diberikan python-compiled script `validate.pyc` yang dapat didekompilasi menggunakan `uncompyle6`,

    ```py
    ❯ uncompyle6 validate.pyc
    # uncompyle6 version 3.7.4
    # Python bytecode 2.7 (62211)
    # Decompiled from: Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
    # [GCC 9.3.0]
    # Embedded file name: validate.py
    # Compiled at: 2021-03-16 13:26:57


    def validate_pin(char):
        if char[0] + char[5] != 109:
            return False
        if char[4] - char[1] % char[3] != 5:
            return False
        if char[2] != 50:
            return False
        if char[5] + char[4] % char[0] != 58:
            return False
        if char[2] + char[3] != 105:
            return False
        if char[1] != 48:
            return False
        if char[2] + char[0] != 102:
            return False
        if char[3] - char[1] != 7:
            return False
        if char[4] % char[5] != 53:
            return False
        if char[4] - char[3] * char[2] != -2697:
            return False
        if char[5] + char[0] != 109:
            return False
        if char[1] != 48:
            return False
        if char[2] % char[5] != 50:
            return False
        if char[3] + char[0] != 107:
            return False
        if char[1] % char[4] != 48:
            return False
        return True


    if __name__ == '__main__':
        pin = raw_input('Enter pin: ')
        if len(pin) == 6:
            if validate_pin(map(ord, pin)):
                print 'Correct Pin!'
                print 'Flag: LKS2021{%s}' % pin
            else:
                print 'Incorrect Pin!'
        else:
            print 'Must be 6-digit pin'
    # okay decompiling validate.pyc
    ```
- Analisis pada kode hasil dekompilasi menunjukkan bahwa terdapat pengecekan 6-digit pin
- Selain itu terdapat fungsi `validate_pin()` yang mana mendeklarasikan beberapa constraint pengecekan pin.
- Penyelesaian dapat dilakukan dengan memasukkan constraint `python-z3` atau melakukan bruteforce digit character menggunakan `nested-loop` sederhana.

## Flag

LKS2021{402759}