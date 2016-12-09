#!/usr/bin/python

import sys
from codecs import decode
"""
Daedalus Corporation encryption script.
"""

def xor(input_data, key):
    result = ""
    for ch in input_data:
        result += chr(ord(ch) ^ key)

    return result

def encrypt(input_data, password):
    key = 0
    for ch in password:
        key ^= ((2 * ord(ch) + 3) & 0xff)

    return xor(input_data, key)
def hacked_encrypt(input_data, password):
	result_list = []
	for key in range(0,256):
		result = xor(input_data, key)
		print "key : {} \t xored : {}".format(key, result)
		result_list.append(result)
	return result_list
def decrypt(input_data, password):
    #return encrypt(input_data, password)
	return hacked_encrypt(input_data, password)

def usage():
    print("Usage: %s [encrypt/decrypt] [in_file] [out_file] [password]" % sys.argv[0])
    exit()

def main():
    if len(sys.argv) < 5:
        usage()

    input_data = open(sys.argv[2], 'r').read()
    result_data = ""
    result_data_list = []
    if sys.argv[1] == "encrypt":
        result_data = encrypt(input_data, sys.argv[4])
    elif sys.argv[1] == "decrypt":
        result_data_list = decrypt(input_data, sys.argv[4])
    else:
        usage()
	#print result_data
    out_file = open(sys.argv[3], 'w')
    for _data in result_data_list:
		out_file.write(_data) 
		out_file.write("\n")
    out_file.close()

main()
