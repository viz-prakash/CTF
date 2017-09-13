# ASIS CTF Final: Simple Crypto

**Category:** Cryptography
**Points:** 34
**Total Solves:** Not Available
## Problem Description:

> Begining always needs an interesting [challenge](simple_crypto_e5189fe3d3d64de3d612de266315a9e96dc43787), we can assure you, this challenge is an interesting one to begin the CTF! Challange Updated, please redownload the binary file!

## Write-up
[//]: # (> Your write up goes here.)
> I started the CTF looking for the easy problems first, clicking on the challange link gave a file named [simple\_crypto\_e5189fe3d3d64de3d612de266315a9e96dc43787](simple\_crypto\_e5189fe3d3d64de3d612de266315a9e96dc43787). `file` command tells that file compressed file in .xz format. 

```
CTF/asisctf/Simple Crypto$ file simple_crypto_e5189fe3d3d64de3d612de266315a9e96dc43787
simple_crypto_e5189fe3d3d64de3d612de266315a9e96dc43787: XZ compressed data
```

> Uncompressing the file with command `tar -xf simple_crypto_e5189fe3d3d64de3d612de266315a9e96dc43787` gives a tar file, and further uncompressing the tar file gives a directory `simple_crypto` which contains two files `flag.enc and simple.py`. Now task looks simple, that is to decode the [flag.enc](simple_crypto/flag.enc) file with the help of [simple.py](simple_crypto/flag.enc), which is probably used to encode it, and get the flag. Looking at code in simple.py tells us that it uses a hardcoded key to xor the hex of original content with expanding the key till length of content of flag and do bit more simple operations. The trick is xoring again the encoded content with expanded key, which hex of hardcoded key and repeating it to the length of content will give us back the original content of flag.enc. This is simple xor logic:

```
if C = A^B then, B = C^A and A = C ^ B.
```

> Code to do this in Python script [simple\_decoder.py](simple_decoder.py). Decoded content is saved in a file, and running `file` on the decoded content tells that it's PNG image file.

```
CTF/asisctf/Simple Crypto$ file simple_crypto/decoded_flag
simple_crypto/decoded_flag: PNG image data, 1842 x 74, 8-bit colormap, non-interlaced
```
> Opening the image gives the flag:
![Image](decoded_flag?raw=true "Flag")

## Other write-ups and resources

* None
