import sys

text_to_morse = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ':'/'}

morse_to_text = dict((v, k) for k, v in text_to_morse.items())

def encrypt_text(msg):

     secret = ""      
     for char in msg.upper():
          secret += text_to_morse[char] + " "
     
     return secret

def decrypt_text(secret):

     msg = ""
     # read until space is reached
     i = 0
     while i < len(secret):
          if secret[i].strip():
               char = ""
               while secret[i].strip():
                    char += secret[i]
                    i += 1 # not incrementing i, interesting
               msg += morse_to_text[char]
          i+=1

     return msg
     
if len(sys.argv)>2:
     if sys.argv[1] == 'e':
          print(encrypt_text(sys.argv[2]))
     elif sys.argv[1] == 'd':
          print(decrypt_text(sys.argv[2]))
     else:
          print("valid methods: e/d")
else:
     print("usage: python3 morse.py <e/d> <msg>")