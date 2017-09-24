import hashlib
import sys

def xor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def repeat(s, l):
    return (s*(int(l/len(s))+1))[:l]

"""
key = sys.argv[1]
plaintext = sys.argv[2] + key
plaintext += hashlib.md5(plaintext).hexdigest()
cipher = xor(plaintext, repeat(key, len(plaintext)))
print cipher.encode('hex')
"""


key = "flag{"
key = "A qua"
def decryption(filename):
	with open(filename) as handle:
		content = handle.read()
	content = content[:-1].decode('hex')
	print("Encoded content length: {}".format(len(content)))
	print("Encoded content lenght with out md5: {}".format(len(content[:-32])))
	deciphered = xor(content, repeat(key, len(content)))
	print("plaintext + key: " + deciphered[:-32])
	print("md5: " + deciphered[-32:])

import string
def is_hex(s):
     hex_digits = set(string.hexdigits)
     # if s is long, then it is faster to check against a set
     return all(c in hex_digits for c in s)

def leaker(filename):
	with open(filename) as handle:
		content = handle.read()
	ciphertext = content[:-1].decode('hex')
	for i in xrange(105,len(ciphertext), 1):
		decoded = xor(ciphertext[i: i + len(key)], key)
		#print("{2}: {0}:hex {1}".format(decoded, ":".join("{:02x}".format(ord(c)) for c in decoded), i))
		#decoded.decode('hex')
		if is_hex(decoded):
			print("{2}: {0}:hex {1}".format(decoded, ":".join("{:02x}".format(ord(c)) for c in decoded), i))

if __name__ == "__main__":
	#decryption(sys.argv[1])
	leaker(sys.argv[1])