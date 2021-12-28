

ALPHAPET = ['\\', '9', '@', 'B', 'c', '0', 'C', 'E', 'e', 'F', '&',  'f',  'g', 'H', ')', 'I', '/', 'J', 'l',  'h',  'j', ',', '=', '<', 'K', '?', 'k', 'M', 'n', 'o', 'P', '}', 'Q', 'q', 'R', '~', 'r', 's', 'T', 't', 'U', 'u', 'D', 'V', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'v', 'z', '2', '3', '4', '5', '6', '7',
            '8', 'a', '!', 'A',  '#', '$', 'b', '%', 'S', 'd',  '^', '*', '(', 'G', '_', '-', '+', 'i', '|', '.', '>', '"', 'L',  "'", ':', ';', '[', '`', '{', 'm',  'O', 'N', ']', 'p',  '1']


def encrypt(string):
    hashed = ''
    for char in string:
        if char in ALPHAPET:
            n = ALPHAPET.index(char)
            hashed += ALPHAPET[-n]
    print(hashed)
    return hashed


def decrypt(hashed):
    string = ""
    for char in hashed:
        if char in ALPHAPET:
            n = ALPHAPET.index(char)
            n = len(ALPHAPET) - n
            n = -n
            string += ALPHAPET[-n]
    print(string)
    return string


decrypt(encrypt('Feras'))
