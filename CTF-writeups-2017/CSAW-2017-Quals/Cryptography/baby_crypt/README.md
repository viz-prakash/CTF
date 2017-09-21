# CSAW-2017 Qualifiers: baby\_crypt

**Category:** Cryptography
**Points:** 350
**Total Solves:** 224
## Problem Description:

![Image](Problem_statement.PNG?raw=true "Problem Statement")

[//]: # (> This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found [here](format.c\).)

## Write-up
[//]: # (> Your write up goes here.)
> After spending hours in solving "Another Xor" problem I was bit motivated to this problem. Problem description was pretty simple, and made clear that breaking the encryption will give the flag. In the description it said: used algorithm is AES ECB, its big relief and I will explain why. ECB mode is bad for encryption. AES ECB mode divides the given input into 16 byte blocks and does the encryption of each block seperately generating 16 byte of output for each block, at the end append the result of encryption of each block in one final encrypted cipher. This is bad because if we provide the same input everytime its going to be encrypted to same output, don't get confuse it with that encryption of same input is same for all algorithms, that's true, but if we can manage to provide the block of input in a way that repeats twice at certain positions ECB mode will generate same cipher for those block of input at that positions, that's not true with other modes. That makes ECB susceptible to replay attacks. You might have seen the encryption of linux image being encrypted but still recognisable becasue of this problem. Now I will explain how we exploit this weakness of ECB to break the encryption.

> System where you can give input for encryption and get an output without any restriction on number of times you can give input, is called oracle. In this problem we are given the oracle running at `crypto.chal.csaw.io 1578`. I mentioned earlier that input is divided into 16 byte block and each block is encrypted seperately, the question comes what if last block doesn't have a 16 bytes? In that case you need to pad the input so that last block will have 16 bytes. Keeping this in mind, if we provide input of 1-16 bytes, size of output will be 16 bytes. But, as problem told us flag is appended to the input, and if flag is bigger than or equals to 16 bytes, and if we give input of 1 byte we will get output cipher of 32 bytes. If flag is less than 16 byte for same 1 byte input we will get 16 bytes of output as cipher, by padding the input + flag to 16 bytes. Considering this, tried to give a input of 1 byte to problem's oracle and tried to analyze the output.

```
/CTF/CSAW-2017/baby_crypt$ nc crypto.chal.csaw.io 1578
Enter your username (no whitespace): a
Your Cookie is: 6673b7dcb699efd844cd79813fc1817a3c67264b74ebcfc1e814b5d1b5d2c784bc4a388b7d1654e782f5f8b55daa7642

CTF/CSAW-2017/baby_crypt$ echo "6673b7dcb699efd844cd79813fc1817a3c67264b74ebcfc1e814b5d1b5d2c784bc4a388b7d1654e782f5f8b55daa7642" | wc -c
97
```

> For giving the input of 1 byte we got output of 48 bytes. wc also counts the null character in it's ouput, and output is in hex, for those who don't know just trust me as 1 byte of input is 2 charcters in hex representation, that's how output is of 48 bytes. This give the useful information that flag is minimum 32 byte in length, 1 character is 1 bytes so, minimum 32 characters long. Let's pin the exact length of flag as a first task. How that can be find out is just keep incrementing the input size by one byte in each input and for the length where output increase from 48 bytes to 64, subtract that length from 48 and additional - 1 will give the flag length. Using this method determined length of flag is 32 bytes as input changed on 17th byte. Now comes the real part of problem, how to break the encryption? As mentioned in the begining same 16 block of input is going to give the same 16 block of output, if we can push 1 character from flag to next block of input, let's say that character is X, last block of input will X + 15 bytes of padding. First we need to figure out what possible padding is used in the oracle? As we know that last character of flag will be '}', adding 15 bytes of our guess padding at the end of `}`  and additional char to push the '}' from 32 byte flag to next block can help us in guessing the padding. Guessing the most obvious padding consisting of 0, input is: `}0000000000000000` known `}` + 15\*0 and extra char 0. Let's see the output:

```
/CTF/CSAW-2017/baby_crypt$ nc crypto.chal.csaw.io 1578
Enter your username (no whitespace): }0000000000000000
Your Cookie is: bc4a388b7d1654e782f5f8b55daa7642846fb11ff58623ed8de20550deb59ef63c67264b74ebcfc1e814b5d1b5d2c784bc4a388b7d1654e782f5f8b55daa7642
```

> Looking at the output we can see the first 16 bytes or 32 hex chars are exactly same as last 16 bytes or 32 chars. That confirms that `padding is of 0` and `last character of flag is }`. In this way we can keep pushing out one character from flag to last block and try all the combination of possible characters in first block, and whatever char input in first block gives same ouput as last block that's character pushed from flag to last block.
Script to solve this is added here [AES-ECB-Decryptor](aes_decryptor.py).

> Flag is: `flag{Crypt0_is_s0_h@rd_t0_d0...}`



## Other write-ups and resources

* None
