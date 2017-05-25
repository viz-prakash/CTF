# Pico-CTF 2014: ZOR

**Category:** Cryptography
**Points:** 50
**Total Solves:** Not Available
## Problem Description:

[//]: # (> This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found [here](format.c\).)
> Daedalus has encrypted their blueprints! Can you get us the password? 
[ZOR.py](ZOR.py)
[encrypted](https://picoctf.com/api/autogen/serve/encrypted?static=false&pid=75648af599de2ecff06e8b74e5fd15c2)

## Write-up
[//]: # (> Your write up goes here.)
```python
#!/usr/bin/python

import sys

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

def decrypt(input_data, password):
    return encrypt(input_data, password)

def usage():
    print("Usage: %s [encrypt/decrypt] [in_file] [out_file] [password]" % sys.argv[0])
    exit()

def main():
    if len(sys.argv) < 5:
        usage()

    input_data = open(sys.argv[2], 'r').read()
    result_data = ""

    if sys.argv[1] == "encrypt":
        result_data = encrypt(input_data, sys.argv[4])
    elif sys.argv[1] == "decrypt":
        result_data = decrypt(input_data, sys.argv[4])
    else:
        usage()

    out_file = open(sys.argv[3], 'w')
    out_file.write(result_data)
    out_file.close()

main()
```
> encrypt function creates a key by doing xor of every character of password with 0xff, so at the end for password there are only 256 options from 0-255.
adding a function which iterate through all the possible keys and decrypting the encoded content with gives the solution.

```python
def hacked_encrypt(input_data, password):
	result_list = []
	for key in range(0,256):
		result = xor(input_data, key)
		print "key : {} \t xored : {}".format(key, result)
		result_list.append(result)
	return result_list
```

> Full solution is in [file](ZOR-Solution.py)

> doing a grep for password in file : 
```bash
grep -a "password" decrypted_content
This message is for Daedalus Corporation only. Our blueprints for the Cyborg are protected with a password. That password is a9db4e0b414b349ef1cbde01858cc1
```
> Flag is : **a9db4e0b414b349ef1cbde01858cc1**
## Other write-ups and resources

* None
