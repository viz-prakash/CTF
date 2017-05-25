# Pico-CTF 2014: Caesar

**Category:** Cryptography
**Points:** 20
**Total Solves:** Not Available
## Problem Description:

[//]: # (> This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found [here](format.c\).)
> You find an encrypted message written on the documents. Can you decrypt it?
> Encrypted content is: `xliwigvixtewwtlvewimwewtlonvlbuuihprubmdpcomvxkjxkd`

## Write-up
[//]: # (> Your write up goes here.)
>> Details on Caeser Cipher: Caeser cipher is technique in which every character in a given is shifted byby fixed count. For eg. text is ABC and fixed count used for shifting is 4, then cipher will be EFG. So, for every character there are 25 options excluding itself. If after shift character position goes more than 26 we take modulus of 26.
> So to solve our problem we can use any [online tool](http://www.xarg.org/tools/caesar-cipher/) and look for all 25 possible shifts.

> In our case shift is of 22 and decrypted plain text is : `thesecretpassphraseisasphkjrhxqqedlnqxizlykirtgftgz`

## Other write-ups and resources

* None
