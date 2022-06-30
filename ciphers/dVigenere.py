import string
import sys

def square(alphabet):
	square = []
	for j in range(26):
		row = ""

		for i in range(j, j+26):
			row += alphabet[i%26]

		square.append(row)

	return square

def create_squares():
	usquare = square(string.ascii_uppercase)
	lsquare = square(sring.ascii_lowercase)

	return (usquare, lsquare)

def decrypt(cipher, key):
	usq, lsq = create_squares()
	print(usq, lsq)
	word = ""
	for i in range(len(cipher)):

		if cipher[i].upper() == cipher[i]:
			col = lsq[0].index(key[i])
			letter = usq[0][usq[col].index(cipher[i])]
		else:
			col = lsq[0].index(key[i])
			letter = lsq[0][lsq[col].index(cipher[i])]

		word += letter

	return word

if len(sys.argv)<2:
	print("Usage: python dVigenere.py <cipher> <key>")
else:
	cipher = sys.argv[1]
	key = sys.argv[2]
	print(decrypt(cipher, key))