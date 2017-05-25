# Pico-CTF 2014: RSA

**Category:** Cryptography
**Points:** 80
**Total Solves:** Not Available
## Problem Description:

[//]: # (> This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found [here](format.c\).)
> A Daedalus Corp spy sent an RSA-encrypted message. We got their key data, but we're not very good at math. Can you decrypt it? [Here's](https://picoctf.com/problem-static/crypto/RSA/handout.tgz) the data. Note that the flag is not a number but a number decoded as ASCII text.

## Write-up
[//]: # (> Your write up goes here.)
In handout we are given RSA arguments
```
N = 0xb197d3afe713816582ee988b276f635800f728f118f5125de1c7c1e57f2738351de8ac643c118a5480f867b6d8756021911818e470952bd0a5262ed86b4fc4c2b7962cd197a8bd8d8ae3f821ad712a42285db67c85983581c4c39f80dbb21bf700dbd2ae9709f7e307769b5c0e624b661441c1ddb62ef1fe7684bbe61d8a19e7
e = 65537
p = 0xc315d99cf91a018dafba850237935b2d981e82b02d994f94db0a1ae40d1fc7ab9799286ac68d620f1102ef515b348807060e6caec5320e3dceb25a0b98356399
q = 0xe90bbb3d4f51311f0b7669abd04e4cc48687ad0e168e7183a9de3ff9fd2d2a3a50303a5109457bd45f0abe1c5750edfaff1ad87c13eed45e1b4bd2366b49d97f
d = 0x496747c7dceae300e22d5c3fa7fd1242bda36af8bc280f7f5e630271a92cbcbeb7ae04132a00d5fc379274cbce8c353faa891b40d087d7a4559e829e513c97467345adca3aa66550a68889cf930ecdfde706445b3f110c0cb4a81ca66f8630ed003feea59a51dc1d18a7f6301f2817cb53b1fb58b2a5ad163e9f1f9fe463b901
```
> We are given N(modulus), Private part E, Public part D, and both prime numbers p and q which is used to generate N, N=p\*q.
> To decrypt the RSA encrypted cipher we use the construct M= (C^d)%N. That is exactly what python script [RSA_calculation.py](RSA_calculation.py) does.

```python
import gmpy2, libnum, binascii
import key_data
import sys

def main():
	f=open(sys.argv[1], "r")
	cipher_str=f.read()
	print "cipher going to be decrypted: ", cipher_str
	cipher=int(cipher_str,16)
	msg=gmpy2.powmod(cipher,key_data.d,key_data.N)
	print "decrypted string : ", libnum.n2s(msg)

if __name__ == "__main__":
	main()
```

```bash
python RSA_calculation.py ciphertext.txt
cipher going to be decrypted:  58ae101736022f486216e290d39e839e7d02a124f725865ed1b5eea7144a4c40828bd4d14dcea967561477a516ce338f293ca86efc72a272c332c5468ef43ed5d8062152aae9484a50051d71943cf4c3249d8c4b2f6c39680cc75e58125359edd2544e89f54d2e5cbed06bb3ed61e5ca7643ebb7fa04638aa0a0f23955e5b5d9
decrypted string :  Congratulations on decrypting an RSA message! Your flag is modular_arithmetics_not_so_bad_after_all
```
> Flag is **modular_arithmetics_not_so_bad_after_all**
## Other write-ups and resources

* None
