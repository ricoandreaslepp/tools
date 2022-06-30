import string
import sys

def rot13(method, text):
    if method == 'e':
        encrypt_rot13 = str.maketrans( 
            "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
            "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
        return str.translate(text, encrypt_rot13)

    elif method == 'd':
        decrypt_rot13 = str.maketrans(
            "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
            "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")
        return str.translate(text, decrypt_rot13)
    else:
        return "valid methods: e/d"

if len(sys.argv)>2:
    for i in range(2, len(sys.argv)):
        print(rot13(sys.argv[1], sys.argv[i]), end=" ")
    print()
else:
    print("usage: python3 rot13.py <e/d> <msg with spaces>")